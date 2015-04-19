# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProjectMember'
        db.create_table(u'walkthrough_projectmember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('owner', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='members', to=orm['walkthrough.Project'])),
        ))
        db.send_create_signal(u'walkthrough', ['ProjectMember'])

        # Adding field 'Project.event'
        db.add_column(u'walkthrough_project', 'event',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ProjectMember'
        db.delete_table(u'walkthrough_projectmember')

        # Deleting field 'Project.event'
        db.delete_column(u'walkthrough_project', 'event')


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
            'event': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'key': ('randomslugfield.fields.RandomSlugField', [], {'exclude_lower': 'False', 'exclude_digits': 'False', 'exclude_vowels': 'False', 'exclude_upper': 'True', 'length': '6', 'max_length': '6', 'blank': 'True', 'unique': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "['name', 'key']", 'overwrite': 'False'}),
            'started': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'tools': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'validate_customer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'validate_offering': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'validate_value_prop': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'walkthrough.projectmember': {
            'Meta': {'object_name': 'ProjectMember'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'owner': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'members'", 'to': u"orm['walkthrough.Project']"})
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