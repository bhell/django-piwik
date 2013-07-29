# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Settings'
        db.create_table(u'piwik_settings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('analyticsSite', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['piwik.Analytics'])),
            ('setting', self.gf('django.db.models.fields.CharField')(max_length='3')),
            ('value', self.gf('django.db.models.fields.CharField')(max_length='255')),
        ))
        db.send_create_signal(u'piwik', ['Settings'])


    def backwards(self, orm):
        
        # Deleting model 'Settings'
        db.delete_table(u'piwik_settings')


    models = {
        u'piwik.analytics': {
            'Meta': {'ordering': "['site']", 'object_name': 'Analytics'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pk_site_id': ('django.db.models.fields.IntegerField', [], {}),
            'pk_tracking_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'site': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sites.Site']", 'unique': 'True'})
        },
        u'piwik.settings': {
            'Meta': {'object_name': 'Settings'},
            'analyticsSite': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['piwik.Analytics']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'setting': ('django.db.models.fields.CharField', [], {'max_length': "'3'"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': "'255'"})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['piwik']
