# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Author'
        db.create_table('db_author', (
            ('website', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('db', ['Author'])

        # Adding model 'Tag'
        db.create_table('db_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('db', ['Tag'])

        # Adding model 'Construction'
        db.create_table('db_construction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('db', ['Construction'])

        # Adding model 'Project'
        db.create_table('db_project', (
            ('depth', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('capacity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('length', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('client', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('annotation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('stocks', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('db', ['Project'])

        # Adding M2M table for field authors on 'Project'
        db.create_table('db_project_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['db.project'], null=False)),
            ('author', models.ForeignKey(orm['db.author'], null=False))
        ))
        db.create_unique('db_project_authors', ['project_id', 'author_id'])

        # Adding M2M table for field constructions on 'Project'
        db.create_table('db_project_constructions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['db.project'], null=False)),
            ('construction', models.ForeignKey(orm['db.construction'], null=False))
        ))
        db.create_unique('db_project_constructions', ['project_id', 'construction_id'])

        # Adding M2M table for field tags on 'Project'
        db.create_table('db_project_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['db.project'], null=False)),
            ('tag', models.ForeignKey(orm['db.tag'], null=False))
        ))
        db.create_unique('db_project_tags', ['project_id', 'tag_id'])

        # Adding model 'ProjectImage'
        db.create_table('db_projectimage', (
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['db.Project'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('db', ['ProjectImage'])

        # Adding model 'Reference'
        db.create_table('db_reference', (
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='references', to=orm['db.Project'])),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('db', ['Reference'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Author'
        db.delete_table('db_author')

        # Deleting model 'Tag'
        db.delete_table('db_tag')

        # Deleting model 'Construction'
        db.delete_table('db_construction')

        # Deleting model 'Project'
        db.delete_table('db_project')

        # Removing M2M table for field authors on 'Project'
        db.delete_table('db_project_authors')

        # Removing M2M table for field constructions on 'Project'
        db.delete_table('db_project_constructions')

        # Removing M2M table for field tags on 'Project'
        db.delete_table('db_project_tags')

        # Deleting model 'ProjectImage'
        db.delete_table('db_projectimage')

        # Deleting model 'Reference'
        db.delete_table('db_reference')
    
    
    models = {
        'db.author': {
            'Meta': {'object_name': 'Author'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'db.construction': {
            'Meta': {'object_name': 'Construction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'db.project': {
            'Meta': {'object_name': 'Project'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'annotation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['db.Author']", 'null': 'True', 'blank': 'True'}),
            'capacity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'client': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'constructions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['db.Construction']", 'null': 'True', 'blank': 'True'}),
            'depth': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'stocks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['db.Tag']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'db.projectimage': {
            'Meta': {'object_name': 'ProjectImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['db.Project']"})
        },
        'db.reference': {
            'Meta': {'object_name': 'Reference'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'references'", 'to': "orm['db.Project']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'db.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }
    
    complete_apps = ['db']
