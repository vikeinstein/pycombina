from abc import ABCMeta, abstractmethod, abstractproperty

class CombinaMilpSolverBaseClass(object):

    __metaclass__ = ABCMeta


    def get_eta(self):

        return self.eta

    def get_b_bin(self):

        return self.b_bin


    def __init__(self, Tg, b_rel, N_c, N_b):

        self.Tg = Tg
        self.b_rel = b_rel
        
        self.N_c = N_c
        self.N_b = N_b


    def setup_sigma_max(self, sigma_max):

        self.sigma_max = sigma_max


    def initialize_model(self):

        self.model = self.Model("Combinatorial Integral Approximation MILP")


    def setup_model_variables(self):

        self.eta_sym = self.model.addVar(vtype = "C", name = "eta")

        self.b_bin_sym = {}
        self.s = {}

        for i in range(self.N_c):
        
            for j in range(self.N_b-1):

                self.s[(i,j)] = self.model.addVar(vtype = "C", \
                    name = "s_{0}".format((i,j)))

                self.b_bin_sym[(i,j)] = self.model.addVar( \
                    vtype = "B", name = "b_bin_{0}".format((i,j)))

            self.b_bin_sym[(i, self.N_b-1)] = self.model.addVar( \
                vtype = "B", name = "b_bin_{0}".format((i,self.N_b-1)))

        
    def setup_objective(self):

        self.model.setObjective(self.eta_sym)


    @abstractmethod
    def setup_maximum_switching_constraints(self):

        r'''
        We set up only the relevant facets, see:
        Sager et al.: Combinatorial integral approximation, 2010
        '''


    @abstractmethod
    def setup_approximation_inequalites(self):
        
        pass


    def setup_milp(self):

        self.initialize_model()
        self.setup_model_variables()
        self.setup_objective()
        self.setup_maximum_switching_constraints()
        self.setup_approximation_inequalites()


    @abstractmethod
    def solve_milp(self):
        
        pass


    @abstractmethod
    def retrieve_solutions(self):
        
        pass


    def run(self, sigma_max):

        self.setup_sigma_max(sigma_max)
        self.setup_milp()
        self.solve_milp()
        self.retrieve_solutions()


class CombinaScipSolver(CombinaMilpSolverBaseClass):

    from pyscipopt import Model, quicksum

    def setup_maximum_switching_constraints(self):

        for i in range(self.N_c):

            for j in range(self.N_b-1):

                self.model.addCons(self.s[(i,j)] >= self.b_bin_sym[(i,j)] - self.b_bin_sym[(i,j+1)])
                self.model.addCons(self.s[(i,j)] >= -self.b_bin_sym[(i,j)] + self.b_bin_sym[(i,j+1)])
                self.model.addCons(self.s[(i,j)] <= self.b_bin_sym[(i,j)] + self.b_bin_sym[(i,j+1)])
                self.model.addCons(self.s[(i,j)] <= 2 - self.b_bin_sym[(i,j)] - self.b_bin_sym[(i,j+1)])

        for i, sigma_max_i in enumerate(self.sigma_max):

            if sigma_max_i % 2 == 0:

                self.model.addCons(sigma_max_i >= self.b_bin_sym[(i,0)] - \
                    self.b_bin_sym[(i,self.N_b-1)] + self.quicksum([self.s[(i,j)] for j in range(self.N_b-1)]))
                self.model.addCons(sigma_max_i >= self.b_bin_sym[(i,self.N_b-1)] - \
                    self.b_bin_sym[(i,0)] + self.quicksum([self.s[(i,j)] for j in range(self.N_b-1)]))

            else:

                self.model.addCons(sigma_max_i >= 1 - self.b_bin_sym[(i,0)] - \
                    self.b_bin_sym[(i,self.N_b-1)] + self.quicksum([self.s[(i,j)] for j in range(self.N_b-1)]))
                self.model.addCons(sigma_max_i >= self.b_bin_sym[(i,0)] + \
                    self.b_bin_sym[(i,self.N_b-1)] - 1 + self.quicksum([self.s[(i,j)] for j in range(self.N_b-1)]))


    def setup_approximation_inequalites(self):

        for i in range(self.N_c):

            for j in range(self.N_b):

                self.model.addCons(self.eta_sym >= self.quicksum( \
                    [self.Tg[k] * (self.b_rel[i][k] - self.b_bin_sym[(i,k)]) for k in range(j)]))
                self.model.addCons(self.eta_sym >= -self.quicksum( \
                    [self.Tg[k] * (self.b_rel[i][k] - self.b_bin_sym[(i,k)]) for k in range(j)]))


    def solve_milp(self):

        # self.model.setRealParam("numerics/lpfeastol", 1e-17)
        self.model.optimize()


    def retrieve_solutions(self):

        self.eta = self.model.getVal(self.eta_sym)

        self.b_bin = []

        for i in range(self.N_c):

            self.b_bin.append([abs(round(self.model.getVal( \
                self.b_bin_sym[(i,j)]))) for j in range(self.N_b)])


class CombinaGurobiSolver(CombinaMilpSolverBaseClass):

    from gurobipy import Model, quicksum

    def setup_maximum_switching_constraints(self):

        for i in range(self.N_c):

            for j in range(self.N_b-1):

                self.model.addConstr(self.s[(i,j)] >= self.b_bin_sym[(i,j)] - self.b_bin_sym[(i,j+1)])
                self.model.addConstr(self.s[(i,j)] >= -self.b_bin_sym[(i,j)] + self.b_bin_sym[(i,j+1)])
                self.model.addConstr(self.s[(i,j)] <= self.b_bin_sym[(i,j)] + self.b_bin_sym[(i,j+1)])
                self.model.addConstr(self.s[(i,j)] <= 2 - self.b_bin_sym[(i,j)] - self.b_bin_sym[(i,j+1)])

        for i, sigma_max_i in enumerate(self.sigma_max):

            if sigma_max_i % 2 == 0:

                self.model.addConstr(sigma_max_i >= self.b_bin_sym[(i,0)] - \
                    self.b_bin_sym[(i,self.N_b-1)] + self.quicksum([self.s[(i,j)] for j in range(self.N_b-1)]))
                self.model.addConstr(sigma_max_i >= self.b_bin_sym[(i,self.N_b-1)] - \
                    self.b_bin_sym[(i,0)] + self.quicksum([self.s[(i,j)] for j in range(self.N_b-1)]))

            else:

                self.model.addConstr(sigma_max_i >= 1 - self.b_bin_sym[(i,0)] - \
                    self.b_bin_sym[(i,self.N_b-1)] + self.quicksum([self.s[(i,j)] for j in range(self.N_b-1)]))
                self.model.addConstr(sigma_max_i >= self.b_bin_sym[(i,0)] + \
                    self.b_bin_sym[(i,self.N_b-1)] - 1 + self.quicksum([self.s[(i,j)] for j in range(self.N_b-1)]))


    def setup_approximation_inequalites(self):

        for i in range(self.N_c):

            for j in range(self.N_b):

                self.model.addConstr(self.eta_sym >= self.quicksum( \
                    [self.Tg[k] * (self.b_rel[i][k] - self.b_bin_sym[(i,k)]) for k in range(j)]))
                self.model.addConstr(self.eta_sym >= -self.quicksum( \
                    [self.Tg[k] * (self.b_rel[i][k] - self.b_bin_sym[(i,k)]) for k in range(j)]))


    def solve_milp(self):

        # self.model.setParam("Presolve", 2)
        self.model.optimize()


    def retrieve_solutions(self):

        self.eta = self.model.getVarByName(self.eta_sym.VarName).x
        
        self.b_bin = []

        for i in range(self.N_c):

            self.b_bin.append([abs(round(self.model.getVarByName( \
                self.b_bin_sym[(i,j)].VarName).x)) for j in range(self.N_b)])
            