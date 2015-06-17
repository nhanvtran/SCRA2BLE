import sys
import re
from singleBin import *

class searchRegion:

	def __init__( self ,name, binLabels, singleBinTags ) :

		self._regionName = name;
		self._binLabels = binLabels;
		self._singleBinTags = singleBinTags;

		self._nBins = len(singleBinTags);
		self._singleBins = [];
		for i in range(self._nBins):
			# print i, self._binLabels[i]
			self._singleBins.append( singleBin(self._regionName + str(i), self._singleBinTags[i], self._binLabels[i], i ) );

		# print "nbins = ", self._nBins;

	def fillRates(self, rateinputs, normalize=False):

		# if len(histograms) != len(self._binLabels): 
		# 	raise Exception("There is a mismatch in histogram input")

		for i in range(self._nBins):
			self._singleBins[i].setRates( rateinputs[i], normalize );
			if len(rateinputs[i]) != len(self._binLabels[i]):
				print  len(rateinputs[i]),len(self._binLabels[i])
				raise Exception("There is a mismatch in this bin of this signal region between rates and n contributions");

		
	def addSingleSystematic(self,sysname,systype,channel,val,identifier='',index=None):
		
		#print "Looking for ",identifier;

		for i in range(self._nBins): 
			#if identifier in self._singleBins[i]._tag:
			if re.search(identifier, self._singleBins[i]._tag) or identifier == '':
				#print "Found! ",self._singleBins[i]._tag;
				if index == None or index == self._singleBins[i]._index:
					# print identifier, " in ", self._singleBins[i]._tag;
					self._singleBins[i].addSystematic( sysname, systype, channel, val );
	def addSystematicByBinTag(self):
		print "this does nothing at the moment"
		
	def setObservedManually(self,listObs):
		for i in range(self._nBins):
			self._singleBins[i]._observed = listObs[i];

	def writeRates(self):
		for i in range(self._nBins):
			self._singleBins[i].writeRates();

	def writeCards(self, odir):
		for i in range(self._nBins):
		# for i in range(4,18):
			# if i!=3 and i!=2: self._singleBins[i].writeCard( odir ); 
			self._singleBins[i].writeCard( odir ); 

	def GetNbins(self):
		return self._nBins;
