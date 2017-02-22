#! /usr/bin/env python

import os
import glob
import math
import array
import sys
import time
import ROOT
from array import array


import tdrstyle
tdrstyle.setTDRStyle()
# ROOT.gROOT.ProcessLine(".L ~/tdrstyle.C");
# ROOT.setTDRStyle();
# ROOT.gStyle.SetPadLeftMargin(0.16);
# ROOT.gStyle.SetPadRightMargin(0.10);
# ROOT.gStyle.SetPadTopMargin(0.10);
# ROOT.gStyle.SetPalette(1);

## ===========================================================================================
## ===========================================================================================
## ===========================================================================================

def columnToList(fn,col):
	f = open(fn,'r');

	olist = [];
	for line in f: 
		linelist = line.strip().split()
		olist.append( linelist[col] );
	return olist

def ExtractFile(iname, tag):
	f = ROOT.TFile(iname);
	t = f.Get("results");
	t.GetEntry(0);
	lims = [];
	lims.append(tag);
	lims.append( t.limit_m2s )
	lims.append( t.limit_m1s );
	lims.append( t.limit_exp )
	lims.append( t.limit_p1s );
	lims.append( t.limit_p2s )
	lims.append( t.limit_obs );
	return lims;

if __name__ == '__main__':

	#idir = "/eos/uscms/store/user/ntran/SUSY/statInterp/scanOutput/Dec6";
	idir = "/eos/uscms/store/user/rgp230/SUSY/statInterp/scanOutput/Moriond/";

	results = [];
	#results.append( ExtractFile(idir+'/results_T2tt_175_1_mu0.0.root','175') );
	results.append( ExtractFile(idir+'/results_T2tt_200_25_mu0.0.root','200') );
	results.append( ExtractFile(idir+'/results_T2tt_225_50_mu0.0.root','225') );
	results.append( ExtractFile(idir+'/results_T2tt_250_75_mu0.0.root','250') );
	results.append( ExtractFile(idir+'/results_T2tt_275_100_mu0.0.root','275') );
	results.append( ExtractFile(idir+'/results_T2tt_300_125_mu0.0.root','300') );
	results.append( ExtractFile(idir+'/results_T2tt_325_150_mu0.0.root','325') );
	results.append( ExtractFile(idir+'/results_T2tt_350_175_mu0.0.root','350') );
	results.append( ExtractFile(idir+'/results_T2tt_375_200_mu0.0.root','375') );
	results.append( ExtractFile(idir+'/results_T2tt_400_225_mu0.0.root','400') );
	results.append( ExtractFile(idir+'/results_T2tt_425_250_mu0.0.root','425') );
	results.append( ExtractFile(idir+'/results_T2tt_450_275_mu0.0.root','450') );
	results.append( ExtractFile(idir+'/results_T2tt_475_300_mu0.0.root','475') );
	results.append( ExtractFile(idir+'/results_T2tt_500_325_mu0.0.root','500') );
	results.append( ExtractFile(idir+'/results_T2tt_525_350_mu0.0.root','525') );
	results.append( ExtractFile(idir+'/results_T2tt_550_375_mu0.0.root','550') );
	results.append( ExtractFile(idir+'/results_T2tt_575_400_mu0.0.root','575') );
	results.append( ExtractFile(idir+'/results_T2tt_600_425_mu0.0.root','600') );
	results.append( ExtractFile(idir+'/results_T2tt_625_450_mu0.0.root','625') );
	results.append( ExtractFile(idir+'/results_T2tt_650_475_mu0.0.root','650') );
	#results.append( ExtractFile(idir+'/results_T1bbbb_1000_800.root','T1bbbb1000') );
	#results.append( ExtractFile(idir+'/results_T1tttt_1500_100.root','T1tttt1500') );
	# results.append( ExtractFile(idir+'/results_T1tttt_1200_800.root','T1tttt1200') );
	#results.append( ExtractFile(idir+'/results_T1tttt_1200_800.root','T1tttt1200') );
	#results.append( ExtractFile(idir+'/results_T1qqqq_1400_100.root','T1qqqq1400') );
	#results.append( ExtractFile(idir+'/results_T1qqqq_1000_900.root','T1qqqq1000') );

	# results.append( ExtractFile(idir+'/results_T1bbbb_1500_100.root','T1bbbb1500') );
	# results.append( ExtractFile(idir+'/results_T1bbbb_1000_100.root','T1bbbb1000') );
	# #results.append( ExtractFile(idir+'/results_T1tttt_1500_100.root','T1tttt1500') );
	# results.append( ExtractFile(idir+'/results_T1tttt_1500_800.root','T1tttt1200') );
	# results.append( ExtractFile(idir+'/results_T1tttt_1200_800.root','T1tttt1200') );
	# results.append( ExtractFile(idir+'/results_T1qqqq_1400_800.root','T1qqqq1400') );
	# results.append( ExtractFile(idir+'/results_T1qqqq_1000_800.root','T1qqqq1000') );

	xsecs=[64.5085,36.3818,21.5949,13.3231,8.51615,5.60471,3.78661,2.61162,1.83537,1.31169,0.948333,0.697075,0.51848,0.390303,0.296128,0.226118,0.174599,0.136372,0.107045];
	names   = [];
	l_obs   = [];
	l_m2sig = [];
	l_m1sig = [];
	l_exp   = [];
	l_p1sig = [];
	l_p2sig = [];
	count=0;
	for r in results:
		names.append(r[0]);
		l_m2sig.append(r[1]*xsecs[count]);
		l_m1sig.append(r[2]*xsecs[count]);
		l_exp.append(r[3]*xsecs[count]);
		l_p1sig.append(r[4]*xsecs[count]);
		l_p2sig.append(r[5]*xsecs[count]);
		l_obs.append(r[6]*xsecs[count]);
		count=count+1
	print "l_exp = ", l_exp
	print "l_obs = ", l_obs

	a_xax = array('d', []);
	a2_xax = array('d', []);
	a_exp = array('d', []);
	a_obs = array('d', []);
	a_1sig = array('d', []);
	a_2sig = array('d', []);

	for i in range(len(names)): a_xax.append( float(i)*25+200 );
	for i in range(len(names)): a2_xax.append( float(i)*25+200 );
	for i in range(len(names)-1,-1,-1): a2_xax.append( float(i)*25+200 );
	for i in range(len(l_obs)): a_obs.append( float(l_obs[i]) );
	for i in range(len(l_exp)): a_exp.append( float(l_exp[i]) );
	
	for i in range(len(l_m2sig)): a_2sig.append( float(l_m2sig[i]) );
	for i in range(len(l_p2sig)-1,-1,-1): a_2sig.append( float(l_p2sig[i]) );
	
	for i in range(len(l_m1sig)): a_1sig.append( float(l_m1sig[i]) );
	for i in range(len(l_p1sig)-1,-1,-1): a_1sig.append( float(l_p1sig[i]) );
	#print a_2sig, len(a_2sig)
	#print a2_xax, len(a2_xax)
	a_2sig.append(results[0][6])
	a2_xax.append(0.5)

	g_exp = ROOT.TGraph(len(a_xax), a_xax, a_exp)
	g_obs = ROOT.TGraph(len(a_xax), a_xax, a_obs)
	g_1sig = ROOT.TGraph(len(2*a_xax), a2_xax, a_1sig)
	g_2sig = ROOT.TGraph(len(2*a_xax), a2_xax, a_2sig)

	print g_2sig;

	can = ROOT.TCanvas("can","can",1400,1000);
	hrl = ROOT.TH1F("hrl","hrl",18,200,650);
	# hrl = can.DrawFrame(0,0,6,15);
	hrl.GetYaxis().SetTitle("95% CL Upper limit on #sigma_{signal} [pb] ");
	hrl.GetXaxis().SetTitle("M_{#tilde{t}} [GeV]");
	#for i in range(0,15):
	#	if i%3==0:
	#		hrl.GetXaxis().SetBinLabel(i+1,names[i])
	#	if i==14:hrl.GetXaxis().SetBinLabel(i+1, names[i])
	#hrl.GetXaxis().SetBinLabel(2,names[1])
	#hrl.GetXaxis().SetBinLabel(3,names[2])
	#hrl.GetXaxis().SetBinLabel(4,names[3])
	#hrl.GetXaxis().SetBinLabel(5,names[4])
	#hrl.GetXaxis().SetBinLabel(6,names[5])
	hrl.SetMaximum(200.);
	hrl.Draw();

	can.SetGrid(); 
	can.SetLogy();
	txta = ROOT.TLatex(0.65,0.90,"CMS");
	txta.SetNDC();
	txtb = ROOT.TLatex(0.75,0.90,"Preliminary");
	txtb.SetNDC(); txtb.SetTextFont(52);
	txtc = ROOT.TLatex(0.75,0.96,"36.3 fb^{-1} (13 TeV)");
	txtc.SetNDC(); txtc.SetTextFont(42); txtc.SetTextSize(0.04);
	txtd = ROOT.TLatex(0.65,0.85,"M_{#tilde{t}} - M_{#tilde{#chi}^{1}_{0}}=175 GeV");
	txtd.SetNDC(); txtd.SetTextFont(42); txtd.SetTextSize(0.05);
	f=open("LatestXsecSqtSqt.txt", 'r')
	a_stop = array('d', []);
	a_xsec = array('d', []);
	for line in f:
		parse=line.split("|")
		a_stop.append(float(parse[1]));
		a_xsec.append(float(parse[2]))
	g_xsec=ROOT.TGraph(len(a_stop), a_stop, a_xsec)
	leg = ROOT.TLegend(0.20,0.15,0.4,0.35);
	leg.SetFillStyle(1001);
	leg.SetFillColor(0);    
	leg.SetBorderSize(1);  
	# leg.SetNColumns(2);
	leg.AddEntry(g_exp,"expected","l")
	leg.AddEntry(g_obs,"observed","l")
	leg.AddEntry(g_2sig,"expected 2#sigma","f")
	leg.AddEntry(g_1sig,"expected 1#sigma","f")
  	leg.AddEntry(g_xsec, "Theory cross-section", "l") 
	#oneLine = ROOT.TF1("oneLine","1",175,550);
	#oneLine.SetLineColor(ROOT.kRed+2);
	#oneLine.SetLineWidth(2);
	#oneLine.SetLineStyle(1);
	
	g_1sig.SetFillColor(ROOT.kGreen);
	g_1sig.SetFillStyle(3244);
	g_2sig.SetFillColor(ROOT.kYellow);
	g_2sig.SetFillStyle(3244);
	g_exp.SetLineStyle(2);
	g_exp.SetLineWidth(2);
	g_obs.SetLineWidth(2);
	g_2sig.Draw('f');
	g_1sig.Draw('fsames');
	#g_1sig.Draw('f');
	g_obs.Draw('lsames');
	g_exp.Draw('lsames');
	#oneLine.Draw("LSAMES");
	txta.Draw();
	txtb.Draw();
	txtc.Draw();
	txtd.Draw();	
	leg.Draw();
	g_xsec.SetLineStyle(2);
	g_xsec.SetLineColor(ROOT.kBlue);
	g_xsec.Draw("lsame")
	can.SaveAs('brazilT2tt.pdf');

