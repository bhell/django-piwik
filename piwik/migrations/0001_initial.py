# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Analytics'
        db.create_table('piwik_analytics', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sites.Site'], unique=True)),
            ('pk_tracking_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('pk_site_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('piwik', ['Analytics'])


    def backwards(self, orm):
        # Deleting model 'Analytics'
        db.delete_table('piwik_analytics')


    models = {
        'piwik.analytics': {
            'Meta': {'ordering': "['site']", 'object_name': 'Analytics'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pk_site_id': ('django.db.models.fields.IntegerField', [], {}),
            'pk_tracking_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'site': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['sites.Site']", 'unique': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['piwik']