# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'walkthrough_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('started', self.gf('django.db.models.fields.DateTimeField')()),
            ('ended', self.gf('django.db.models.fields.DateTimeField')()),
            ('idea', self.gf('django.db.models.fields.TextField')()),
            ('validate_customer', self.gf('django.db.models.fields.TextField')()),
            ('validate_offering', self.gf('django.db.models.fields.TextField')()),
            ('validate_value_prop', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'walkthrough', ['Project'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'walkthrough_project')


    models = {
        u'walkthrough.project': {
            'Meta': {'object_name': 'Project'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ended': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('django.db.models.fields.TextField', [], {}),
            'project_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'started': ('django.db.models.fields.DateTimeField', [], {}),
            'validate_customer': ('django.db.models.fields.TextField', [], {}),
            'validate_offering': ('django.db.models.fields.TextField', [], {}),
            'validate_value_prop': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['walkthrough']