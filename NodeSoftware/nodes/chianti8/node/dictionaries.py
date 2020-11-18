# -*- coding: utf-8 -*-

from vamdctap.unitconv import invcm2eV
from datetime import date, datetime

# In the RESTRICTABLES dictionary, keys are names from the dictionary and values are 
# names from the Django model for the transitions table.
#
# Where a field is actually in the transitions model (i.e. in the transitions table and
# not in a linked table) then the name of the field appears without punctuation. Where
# the field is in a related model (meaning that Django must join tables to get at it),
# the double-underscore operator expressed the chain of relations.
#
# E.g., radtranswavelengthexperimentalvalue refers a field directly in the transitions model.
# finalstateindex__species__atomsymbol refers to the atomsymbol field in the
# species model. The transitions model has a foreign key to the states model in a field
# called finalstateindex. The states model has a foreign key to the species model in a
# field called species. All three parts of finalstateindex__species__atomsymbol are names of 
# fields in models; names of entire models are not part of this syntax.


def dateToEdition(op, d):
    """
    Converts the date argument for the AsOfDate operand to the equivalent edition-number.
    The argument appears as an ISO date, e.g. 2012-07-01, surrounded by single quotes.
    I.e. the quotes have to be stripped out before parsing the date.
    """
    try:
        print "dateToEdition %s\n"%str(d)
        d1 = datetime.strptime(d[1:11],'%Y-%m-%d')
        if d1 < datetime(2016,1,24,0,0,0):
            print "edition 1\n"
            return [op, '1']
        else:
            print "edition 2\n"
            return [op, '2']
    except BaseException, e:
        print'Date is no good: %s\n'%str(e)

RESTRICTABLES = {\
'AtomSymbol':'finalstateindex__species__atomsymbol',
'AtomNuclearCharge':'finalstateindex__species__atomnuclearcharge',
'IonCharge':'finalstateindex__species__atomioncharge',
'StateEnergy':'finalstateindex__energy',
'RadTransWavelength':'wavelength',
'AsOfDate':('finalstateindex__species__edition',dateToEdition)
}

RETURNABLES = {\
'NodeID':u'chianti', # Constant value
'XSAMSVersion':u'1.0',

'MethodID':'Method.id',
'MethodCategory':'Method.category',

'AtomSpeciesId':'Atom.id',
'AtomSymbol':'Atom.atomsymbol',
'AtomNuclearCharge':'Atom.atomnuclearcharge',
'AtomIonCharge':'Atom.atomioncharge',
'AtomInchi':'Atom.inchi',
'AtomInchiKey':'Atom.inchikey',
'AtomStateId':'AtomState.id',
'AtomStateTotalAngMom':'AtomState.atomstatetotalangmom',
'AtomStateParity':'AtomState.parity',
'AtomStateStatisticalWeight':'(2*AtomState.atomstatetotalangmom)+1',
'AtomStateEnergy':'AtomState.energy',
'AtomStateEnergyMethod':'AtomState.energyMethod',
'AtomStateEnergyUnit':u'1/cm',
'AtomStateDescription':'AtomState.atomstateconfigurationlabel',
'AtomStateRef':'AtomState.sourceIds()',

'AtomStateTermLSS':'Component.lss',
'AtomStateTermLSL':'Component.lsl',
#'AtomStateConfigurationLabel':'Component.label',
'AtomStateElementCore':'Component.core',

'AtomStateShellPrincipalQN':'AtomShell.n',
'AtomStateShellOrbitalAngMom':'AtomShell.l',
'AtomStateShellNumberOfElectrons':'AtomShell.population',

'RadTransWavelength':'RadTran.allWavelengths()',
'RadTransWavelengthMethod':'RadTran.allWavelengthMethods()',
'RadTransWavelengthUnit':u'A', # Constant: Angstroms
'RadTransProbabilityWeightedOscillatorStrength':'RadTran.weightedoscillatorstrength',
'RadTransProbabilityA':'RadTran.probabilitya',
'RadTransProbabilityAUnit':u'1/s',
'RadTransSpeciesRef':'RadTran.initialstateindex.species.id',
'RadTransUpperStateRef':'RadTran.upperStateRef()',
'RadTransLowerStateRef':'RadTran.lowerStateRef()',
'RadTransID':'RadTran.id'
}


def radTransWavelength(r):
  return [r.wavelengthexperimental, r.wavelengththeoretical]

