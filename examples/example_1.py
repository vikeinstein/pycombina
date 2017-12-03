#!/usr/bin/python

import pylab as pl
from pycombina import Combina

b_rel = [[9.164991131439303e-08, 9.164989910069793e-08, 9.164986964110127e-08, 9.164981439200778e-08, 9.164971954974675e-08, 9.164956322584703e-08, 9.164931096870898e-08, 9.164890871558705e-08, 9.16482717331077e-08, 9.164726728376491e-08, 9.164568747185336e-08, 9.164320671195729e-08, 9.163931511370584e-08, 9.163321414037958e-08, 9.162365315758747e-08, 9.160867333705047e-08, 9.158520628111474e-08, 9.154844464973005e-08, 9.149085452908308e-08, 9.140062376048531e-08, 9.125921952032561e-08, 9.103753238327347e-08, 9.06897600760712e-08, 9.01436326543539e-08, 8.928459967910412e-08, 8.792973591727924e-08, 8.578323033799388e-08, 8.235606307513253e-08, 7.680620700237228e-08, 6.75611734322906e-08, 5.110029321633913e-08, 4.403564664444702e-08, 4.106387808317555e-08, 3.983950373134124e-08, 3.934055898011604e-08, 3.9137914036044536e-08, 3.9054919200406776e-08, 3.901881246871395e-08, 3.899786135210769e-08, 3.897363059366587e-08, 3.8924779784938846e-08, 3.880822297418e-08, 3.852080876236079e-08, 3.780600129669751e-08, 3.601141047402357e-08, 3.139256276666938e-08, 2.9834455518510574e-08, 2.9318934446262996e-08, 2.914964834988244e-08, 2.9094176453158642e-08, 2.907592834306512e-08, 2.9069660025366436e-08, 2.906669316762665e-08, 2.906291807927123e-08, 2.9053105209808462e-08, 2.9023659839179072e-08, 2.893375174707503e-08, 2.865832883983718e-08, 2.781057309571279e-08, 2.516081216626174e-08, 1.6349821111021932e-08, 1.4641381658496285e-08, 1.4321695524188809e-08, 1.4262451136479392e-08, 1.4251493200337602e-08, 1.4249467289977935e-08, 1.424909202859219e-08, 1.4249016931279371e-08, 1.4248970149529801e-08, 1.4248781586888953e-08, 1.4247771634743814e-08, 1.4242308735857878e-08, 1.4212753082407813e-08, 1.4052702623315826e-08, 1.3181284088570942e-08, 8.268584499081758e-09, 7.688662077381325e-09, 7.621735475505242e-09, 7.61405669269621e-09, 7.613347382291173e-09, 7.614772557847257e-09, 7.628032105221415e-09, 7.743336673082607e-09, 7.774748608050492e-09, 7.781914757778366e-09, 7.777476689145606e-09, 7.768965238198726e-09, 7.809086255912332e-09, 8.347837492600157e-09, 1.3149458138366266e-08, 5.812677816280237e-08, 7.980857140061672e-08, 9.34899928315103e-08, 1.0296318896151463e-07, 1.0994080615953228e-07, 1.1547277950297847e-07, 1.2038557045733308e-07, 1.2548706350691847e-07, 1.3170304260698727e-07, 1.4020750175014196e-07, 1.526048438509999e-07, 1.7130057227378714e-07, 2.005178071994339e-07, 2.499858770490773e-07, 3.5728576775753295e-07, 0.20636133458659084, 0.206361456820869, 0.20636151047209217, 0.20636154006894097, 0.20636155692321392, 0.2063615660721068, 0.2063615709426096, 0.2063615747616593, 0.206361581065729, 0.20636159414396368, 0.2063616208814176, 0.20636168097818755, 0.2063617772714703, 0.2063618582371984, 0.20636189781122233, 0.20636190501221507, 0.2063619496037749, 0.2063620732923192, 0.20636249842130122, 0.2063773813145899, 0.252054864921568, 0.2520579982392464, 0.25288811587249843, 0.2593977742761429, 0.3340935108565165, 0.3340940442516569, 0.33409419385053196, 0.3340942499059316, 0.3340942652728998, 0.33409424511989244, 0.3135810041373855, 0.3135809645281175, 0.31358095939038705, 0.3135809756716781, 0.3135810190249818, 0.31358111927309246, 0.3135814262624077, 0.999999950926087, 0.999999974046433, 0.9999999783613379, 0.9999999789321505, 0.9999999787698426, 0.9999999779052294, 0.9999999747514201, 0.9999999550265595, 0.06453461127561795, 0.06453456953472514, 0.06453456775738621, 0.0645345926266459, 0.06453465796048136, 0.06453481999226998, 0.06453538382656564, 0.2131890930121317, 0.2131936809163467, 0.21319408556528727, 0.21319422088078965, 0.21319427911618313, 0.21319430204287756, 0.2131943004833132, 0.213194265080231, 2.287219254968173e-08, 1.0681031150093401e-08, 9.359002315937822e-09, 9.461200350554808e-09, 9.80570097938495e-09, 1.0901115627326692e-08, 1.2859087591404522e-08, 1.5439876067722526e-08, 1.881147846187437e-08, 2.325425317922466e-08, 2.905700927723151e-08, 3.620161250971683e-08, 4.3709179595637425e-08, 4.8807602615609486e-08, 4.614727473289024e-08, 2.319637525384318e-08, 2.3113256911779592e-08, 3.062367109037491e-08, 4.5803905719390506e-08, 7.373574744184745e-08, 1.249404286368601e-07, 2.24798134068856e-07, 4.5731586084303404e-07, 1.3208173664524378e-06, 0.0433240937001994, 0.04332605093577369, 0.043326318185106925, 0.04332641234938346, 0.043326451830150416, 0.04332646332568629, 0.04332645064755273, 0.043326464881207304, 0.04332652140919314, 0.9999999444789713, 0.9999999847239209, 0.9999999852314699, 0.9999999823896432, 0.9999999805987997, 0.9999999804592423, 0.9999999816949504, 0.9999999837988184, 0.9999999862895442, 0.999999988820378, 0.9999999911927993, 0.9999999933222256, 0.9999999952099605, 0.9999999968647432, 0.9999999982733226, 0.9999999994748296, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9999999976933017, 0.9999999927247275, 0.9999999813465971, 0.9999999516982475, 0.9999998765776738, 0.9999996930339815, 0.999999381480724, 0.9999952329064322, 0.33837190283783086, 0.33836939449774384, 0.33836820191669553, 0.3383674235415369, 0.3383668483297875, 0.3383663939468469, 0.33836601976451697, 0.3383657027491601, 0.3383654285764394, 0.33836518772741186, 0.33836497355245754, 0.3383647812216936, 0.3383646071134709, 0.33836444845465696, 0.3383643046158953, 0.33836417338226865, 0.338364053014526, 0.3383639421153582, 0.33836383954553606, 0.3383637443641662, 0.338363655785219, 0.33836357314532267, 0.33836349587948944, 0.3383634235025246, 0.3383633555945778, 0.3383632917897552, 0.3383632317670245, 0.3383631752430078, 0.3383631219726682, 0.33836307197017373, 0.33836302498944143, 0.3383629808173723, 0.3383629392632571, 0.33836290015502957, 0.33836286333638244, 0.3383628286684003, 0.3383627960634522, 0.3383627654812393, 0.33836273685899004, 0.33836271012357955, 0.3383626852031968, 0.33836266203107024, 0.33836264055345605, 0.33836262073384066, 0.33836260260332357, 0.33836258610656866, 0.33836257119446206, 0.33836255782361746, 0.338362545955937, 0.3383625355582329, 0.3383625266019055, 0.3383625190626729, 0.3383625129203459, 0.33836250815864527, 0.3383625047650565, 0.338362502730721, 0.33836250205035523]]
T = [240 * i for i in range(len(b_rel[0])+1)]
max_switches = [4]

combina = Combina(T, b_rel)
combina.solve(solver = "bnb", max_switches = max_switches, min_up_time = [1200])
b_bin = combina.b_bin

eta = [(0,0)]
Tg = (pl.asarray(T[1:]) - pl.asarray(T[:-1])).tolist()

for k, b_bin_k in enumerate(b_bin):

    for i, b_i in enumerate(b_bin_k):

        eta_i = abs(sum([Tg[j] * (b_rel[k][j] - b_bin_k[j]) for j in range(i)]))

        if eta_i > eta[k][1]:

            eta[k] = (i, eta_i)

pl.figure()
pl.step(T[:-1], b_rel[0])
pl.step(T[:-1], b_bin[0])
pl.show()
