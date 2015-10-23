from ROOT import *

import os
import math
import sys
from searchRegion import *
from singleBin import *

from optparse import OptionParser
parser = OptionParser()
parser.add_option('-b', action='store_true', dest='noX', default=False, help='no X11 windows')
parser.add_option("--signal", dest="signal", default = 'SMSqqqq',help="mass of LSP", metavar="signal")
parser.add_option("--tag", dest="tag", default = 'SinglePhoton1',help="mass of LSP", metavar="tag")
parser.add_option("--mGo", dest="mGo", default='1000', help="Mass of Gluino", metavar="mGo")
parser.add_option("--mLSP", dest="mLSP", default='900', help="Mass of LSP", metavar="mLSP")
(options, args) = parser.parse_args()


#########################################################################################################
def getFittedMu(fn):
	
	output = [];

	tf = TFile(fn);
	tt = tf.Get("limit")
	tt.GetEntry(0);
	output.append( tt.limit );
	tt.GetEntry(1);
	output.append( tt.limit );
	tt.GetEntry(2);
	output.append( tt.limit );

	print output
	return output

def getLimit(fn):

	tf = TFile(fn);
	tt = tf.Get("limit")
	tt.GetEntry(2);
	output = tt.limit;

	return output

def getSignif(fn):
	
	tf = TFile(fn);
	tt = tf.Get("limit")
	tt.GetEntry(0);

	print "[getSignif], ", tt.limit
	return tt.limit;

#########################################################################################################
if __name__ == '__main__':
	
	#signals = ['SMSqqqq1400','SMSqqqq1000']
	#signals = ['SMSqqqq1400']
	#signals = ['SMSbbbb1500','SMSbbbb1000','SMStttt1500','SMStttt1200']	
	signalmodel=options.signal+options.mGo
	signals = [signalmodel]
	#mus = [0.0,0.5,1.0 ,1.5, 2.0, 2.5, 3.0,3.5, 4.0,4.5, 5.0];
	#mus = [10000.0];
	mus=[0.0]
	#lumis = [3.0,10.0];
	lumis = [225];

	#variations = ['qcdOnly','zvvOnly','llpOnly','tauOnly']
	#variations = ['allNotau','llpOnly', 'tauOnly']
	# variations = ['allBkgs','allNoqcd','allNozvv','allNollp','allNotau']
	#variations=['allNoqcd','allNozvv','allNollp','allNotau']
	#variations = ['qcdOnly' ]
	variations = ['allBkgs']
	#variations=['allNozvv']
	# variations=['onlyLep']
	#variations=['tauOnly']
	#variations=['allBkgs']
	identifiers = [];
	limits = [];
	fittedMus = [];
	injectedMus = [];
	significances = [];

	for lumi in lumis: 
	#os.system("python QuickBias.py %d" %i)

		print "=========>>> LUMI is ", lumi

		for sig in signals:
			for mu in mus:
				for vary in variations: 
					tag = vary;
					combOpt = '';
					if vary == 'allBkgs':  combOpt = '--allBkgs'
					if vary == 'qcdOnly':  combOpt = '--qcdOnly'
					if vary == 'zvvOnly':  combOpt = '--zvvOnly'
					if vary == 'llpOnly':  combOpt = '--llpOnly'
					if vary == 'tauOnly':  combOpt = '--tauOnly'
					if vary == 'allNoqcd': combOpt = '--tauOnly --zvvOnly --llpOnly'
					if vary == 'allNozvv': combOpt = '--tauOnly --qcdOnly --llpOnly'
					if vary == 'allNollp': combOpt = '--tauOnly --zvvOnly --qcdOnly'
					if vary == 'allNotau': combOpt = '--qcdOnly --zvvOnly --llpOnly'
					if vary == 'allNolep': combOpt = '--qcdOnly --zvvOnly'
					if vary == 'onlyLep': combOpt = '--tauOnly --llpOnly'

					command = 'python buildCards-AllBkgsMassScan.py -b %s --signal  %s --tag %s --lumi %0.1f --mu %0.1f --mGo=%s --mLSP=%s' % (combOpt,options.signal,tag,lumi,mu, options.mGo, options.mLSP); os.system(command);
					command = 'python combineAllCards.py -b --run --dir testCards-%s-%s-%0.1f-mu%0.1f' % (tag,sig,lumi,mu); os.system(command);

					dicttag = "%s_%s_%.1f" % (tag,sig,lumi);

					identifiers.append( dicttag );
					#significances.append( getSignif( "higgsCombinetestCards-%s-%s-%0.1f-mu%0.1f.ProfileLikelihood.mH120.root" % (tag,sig,lumi,mu) ) );
					#limits.append( getLimit( "higgsCombinetestCards-%s-%s-%0.1f-mu%0.1f.Asymptotic.mH120.root" % (tag,sig,lumi,mu) ) );
					#fittedMus.append( getFittedMu( "higgsCombinetestCards-%s-%s-%0.1f-mu%0.1f.MaxLikelihoodFit.mH120.root" % (tag,sig,lumi,mu) ) );
					# significances.append( 0. );
					# limits.append( 0. );
					#fittedMus.append( [0.,0.,0.] );
					injectedMus.append( mu );

	for i in range(len(identifiers)):
		splitid = identifiers[i].split('_');
		#print splitid[0],splitid[1],splitid[2],round(fittedMus[i][0],4),round(injectedMus[i],4);
		#print splitid[0],splitid[1],splitid[2],round(injectedMus[i][0],4),round(injectedMus[i],4)




