from __future__ import print_function
import os
import errno
from ROOT import TFile, TH1D, Math, gStyle, THStack, TLegend, TCanvas, TPad, gPad, TLatex, TLine
from bg_est import BGEst
from data_obs import DataObs
from obs_exp_ratio import ObsExpRatio
from agg_bins import AddHistsInQuadrature
import CMS_lumi

plot_dir = "output/"

def make_1d_pull_dist(plot_title, lostlep, hadtau, znn, qcd, data_obs):

    TH1D.SetDefaultSumw2(True)
    import tdrstyle
    tdrstyle.setTDRStyle()
    
    hdata_obs = data_obs.hist
    sumBG = BGEst.sumBG(lostlep, hadtau, znn, qcd)
    hbg_pred = sumBG.hCV
    hbg_err_up = AddHistsInQuadrature('err_up', [sumBG.hStatUp, sumBG.hSystUp])
    hbg_err_down = AddHistsInQuadrature('err_down', [sumBG.hStatDown, sumBG.hSystDown])
    ratio = ObsExpRatio(DataObs(hdata_obs), sumBG)
    pull = ratio.pull

    hpull = TH1D("hPull", ";Pull = [N_{Obs.}-N_{Pred.}] / #sqrt{N_{Pred.}+(#deltaN_{Pred.})^{2}};N_{bins}", 25, -3.25, 3.25)
    hpull.GetXaxis().SetLabelSize(0.035)
    hpull.GetXaxis().SetTitleSize(0.035)
    hpull.GetXaxis().SetTitleOffset(1.3)
    hpull.GetXaxis().SetTitleFont(42)
    hpull.GetYaxis().SetLabelSize(0.04)
    hpull.GetYaxis().SetTitleSize(0.04)
    hpull.GetYaxis().SetTitleOffset(1.15)
    hpull.GetYaxis().SetTitleFont(42)
    hpull.GetYaxis().SetNdivisions(505)
    hpull.GetYaxis().SetTickLength(0.015)
    hpull.GetXaxis().SetTickLength(0.08)
    hpull.SetFillColor(2029)
    hpull.SetLineColor(1)
    hpull.SetLineWidth(2)

    for ibin in range(pull.GetNbinsX()):
        hpull.Fill(pull.GetBinContent(ibin+1))
        if abs(pull.GetBinContent(ibin+1))>1.5:
            print("Bin %d: Obs: %d, Pred: %3.3f, Err: %3.3f - %3.3f, Pull: %3.2f" % (ibin+1, hdata_obs.GetBinContent(ibin+1), hbg_pred.GetBinContent(ibin+1),\
                                                                                       hbg_err_up.GetBinContent(ibin+1), hbg_err_down.GetBinContent(ibin+1),\
                                                                                       pull.GetBinContent(ibin+1)) )

    for ibin in range(hpull.GetNbinsX()):
        if hpull.GetBinContent(ibin+1)>0.:
            hpull.SetBinError(ibin+1,0.0001)

    if hpull.GetBinContent(hpull.GetNbinsX()+1)>0.:
        hpull.SetBinContent(hpull.GetNbinsX(), hpull.GetBinContent(hpull.GetNbinsX())+hpull.GetBinContent(hpull.GetNbinsX()+1))

    W = 800
    H = 800
    T = 0.08*H
    B = 0.15*H 
    L = 0.12*W
    R = 0.04*W
    canv = TCanvas("canvName","canvName", 50, 50, W, H)
    canv.SetFillColor(0)
    canv.SetBorderMode(0)
    canv.SetFrameFillStyle(0)
    canv.SetFrameBorderMode(0)
    canv.SetLeftMargin( L/W )
    canv.SetRightMargin( R/W )
    canv.SetTopMargin( T/H )
    canv.SetBottomMargin( B/H )
    canv.SetTickx(0)
    canv.SetTicky(0) 
    canv.SetFrameFillColor(0)
    canv.SetFillColor(0)
    canv.SetTopMargin(0.12)
    canv.SetLeftMargin(0.1)

    hpull.Draw("hist");

    lumi = 18.077491
##    lumi = 5.2
    CMS_lumi.writeExtraText = True
    CMS_lumi.extraText = "       Preliminary"
    CMS_lumi.lumi_13TeV="%8.1f fb^{-1}" % lumi
    CMS_lumi.lumi_sqrtS = CMS_lumi.lumi_13TeV+ " (13 TeV)"
    CMS_lumi.relPosX = 0.1
    CMS_lumi.relPosY = 0.05
    CMS_lumi.cmsTextSize = 0.5
    iPos=0.75
    CMS_lumi.CMS_lumi(canv, 0, iPos)
 
    canv.Print(plot_dir+plot_title+".pdf")
