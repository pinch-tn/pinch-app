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
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200, db_index=True)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from='name', overwrite=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('started', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('ended', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('idea', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('tools', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('validate_customer', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('validate_offering', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('validate_value_prop', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'walkthrough', ['Project'])

        # Adding model 'Mvp'
        db.create_table(u'walkthrough_mvp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['walkthrough.Project'], unique=True)),
            ('original_statement', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'walkthrough', ['Mvp'])

        # Adding model 'MvpRedaction'
        db.create_table(u'walkthrough_mvpredaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mvp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['walkthrough.Mvp'])),
            ('line', self.gf('django.db.models.fields.IntegerField')()),
            ('statement_start', self.gf('django.db.models.fields.IntegerField')()),
            ('statement_end', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'walkthrough', ['MvpRedaction'])

        # Adding model 'Workstream'
        db.create_table(u'walkthrough_workstream', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mvp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['walkthrough.Mvp'])),
            ('line', self.gf('django.db.models.fields.IntegerField')()),
            ('statement_start', self.gf('django.db.models.fields.IntegerField')()),
            ('statement_end', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('owner', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'walkthrough', ['Workstream'])

        # Adding unique constraint on 'Workstream', fields ['name', 'mvp']
        db.create_unique(u'walkthrough_workstream', ['name', 'mvp_id'])

        # Adding model 'Ticket'
        db.create_table(u'walkthrough_ticket', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mvp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['walkthrough.Mvp'])),
            ('workstream', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['walkthrough.Workstream'])),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'walkthrough', ['Ticket'])


    def backwards(self, orm):
        # Removing unique constraint on 'Workstream', fields ['name', 'mvp']
        db.delete_unique(u'walkthrough_workstream', ['name', 'mvp_id'])

        # Deleting model 'Project'
        db.delete_table(u'walkthrough_project')

        # Deleting model 'Mvp'
        db.delete_table(u'walkthrough_mvp')

        # Deleting model 'MvpRedaction'
        db.delete_table(u'walkthrough_mvpredaction')

        # Deleting model 'Workstream'
        db.delete_table(u'walkthrough_workstream')

        # Deleting model 'Ticket'
        db.delete_table(u'walkthrough_ticket')


    models = {
        u'walkthrough.mvp': {
            'Meta': {'object_name': 'Mvp'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_statement': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'project': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['walkthrough.Project']", 'unique': 'True'})
        },
        u'walkthrough.mvpredaction': {
            'Meta': {'object_name': 'MvpRedaction'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line': ('django.db.models.fields.IntegerField', [], {}),
            'mvp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['walkthrough.Mvp']"}),
            'statement_end': ('django.db.models.fields.IntegerField', [], {}),
            'statement_start': ('django.db.models.fields.IntegerField', [], {})
        },
        u'walkthrough.project': {
            'Meta': {'object_name': 'Project'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ended': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'name'", 'overwrite': 'False'}),
            'started': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'tools': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'validate_customer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'validate_offering': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'validate_value_prop': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'walkthrough.ticket': {
            'Meta': {'object_name': 'Ticket'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mvp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['walkthrough.Mvp']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'workstream': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['walkthrough.Workstream']"})
        },
        u'walkthrough.workstream': {
            'Meta': {'unique_together': "(('name', 'mvp'),)", 'object_name': 'Workstream'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line': ('django.db.models.fields.IntegerField', [], {}),
            'mvp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['walkthrough.Mvp']"}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'owner': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'statement_end': ('django.db.models.fields.IntegerField', [], {}),
            'statement_start': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['walkthrough']