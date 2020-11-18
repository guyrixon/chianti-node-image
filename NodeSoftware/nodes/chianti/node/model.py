# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class States(models.Model):
    chiantiiontype = models.CharField(max_length=3, db_column='ChiantiIonType', blank=True) # Field name made lowercase.
    atomsymbol = models.CharField(max_length=6, db_column='AtomSymbol', blank=True) # Field name made lowercase.
    atomnuclearcharge = models.IntegerField(null=True, db_column='AtomNuclearCharge', blank=True) # Field name made lowercase.
    atomioncharge = models.IntegerField(null=True, db_column='AtomIonCharge', blank=True) # Field name made lowercase.
    chiantiatomstateindex = models.IntegerField(null=False, db_column='ChiantiAtomStateIndex', primary_key=True, blank=True) # Field name made lowercase.
    atomstateconfigurationlabel = models.CharField(max_length=96, db_column='AtomStateConfigurationLabel', blank=True) # Field name made lowercase.
    atomstates = models.FloatField(null=True, db_column='AtomStateS', blank=True) # Field name made lowercase.
    atomstatel = models.FloatField(null=True, db_column='AtomStateL', blank=True) # Field name made lowercase.
    atomstatetotalangmom = models.FloatField(null=True, db_column='AtomStateTotalAngMom', blank=True) # Field name made lowercase.
    atomstateenergyexperimentalvalue = models.FloatField(null=True, db_column='AtomStateEnergyExperimentalValue', blank=True) # Field name made lowercase.
    atomstateenergytheoreticalvalue = models.FloatField(null=True, db_column='AtomStateEnergyTheoreticalValue', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'states'

