# Generated by Django 2.0.5 on 2020-01-11 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swiph', '0003_auto_20200111_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulation',
            name='A_aperture',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='ColAz',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='GeomEffects',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='HL_W_0',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='HL_W_1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='HL_W_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='HL_W_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='HL_W_4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='HL_dT_0',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='HL_dT_1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='HL_dT_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='HL_dT_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='HL_dT_4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='IAM_L0',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='IAM_L1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='IAM_L2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='IAM_L3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='IAM_L4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='IAM_T0',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='IAM_T1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='IAM_T2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='IAM_T3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='IAM_T4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='I_bn_des',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='L_col',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='Pipe_hl_coef',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='SCA_drives_elec',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='T_amb_des_sf',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='T_fp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='TrackingError',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='V_wind_max',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='csp_lf_sf_washes_per_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='csp_lf_sf_water_per_wash',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='dirt_mirror',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='e_startup',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='error',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='eta_pump',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='fP_hdr_c',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='fP_hdr_h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='fP_sf_boil',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='heat_sink_dP_frac',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='rho_mirror_clean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='theta_dep',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='theta_stow',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='x_b_des',
            field=models.FloatField(blank=True, null=True),
        ),
    ]