# Generated by Django 2.1.3 on 2018-11-09 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Credential",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64, unique=True)),
                (
                    "cred_type",
                    models.CharField(
                        choices=[
                            ("network", "network"),
                            ("vcenter", "vcenter"),
                            ("satellite", "satellite"),
                        ],
                        max_length=9,
                    ),
                ),
                ("username", models.CharField(max_length=64)),
                ("password", models.CharField(max_length=1024, null=True)),
                ("ssh_keyfile", models.CharField(max_length=1024, null=True)),
                ("ssh_passphrase", models.CharField(max_length=1024, null=True)),
                (
                    "become_method",
                    models.CharField(
                        choices=[
                            ("sudo", "sudo"),
                            ("su", "su"),
                            ("pbrun", "pbrun"),
                            ("pfexec", "pfexec"),
                            ("doas", "doas"),
                            ("dzdo", "dzdo"),
                            ("ksu", "ksu"),
                            ("runas", "runas"),
                        ],
                        max_length=6,
                        null=True,
                    ),
                ),
                ("become_user", models.CharField(max_length=64, null=True)),
                ("become_password", models.CharField(max_length=1024, null=True)),
            ],
            options={
                "verbose_name_plural": "Credentials",
            },
        ),
        migrations.CreateModel(
            name="DeploymentsReport",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "report_type",
                    models.CharField(
                        choices=[
                            ("details", "details"),
                            ("deployments", "deployments"),
                        ],
                        default="deployments",
                        max_length=11,
                    ),
                ),
                ("report_version", models.CharField(max_length=64)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "pending"),
                            ("failed", "failed"),
                            ("completed", "completed"),
                        ],
                        default="pending",
                        max_length=16,
                    ),
                ),
                ("report_id", models.IntegerField(null=True)),
                ("cached_json", models.TextField(null=True)),
                ("cached_csv", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="DetailsReport",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "report_type",
                    models.CharField(
                        choices=[
                            ("details", "details"),
                            ("deployments", "deployments"),
                        ],
                        default="details",
                        max_length=11,
                    ),
                ),
                ("report_version", models.CharField(max_length=64)),
                ("sources", models.TextField()),
                ("report_id", models.IntegerField(null=True)),
                ("cached_csv", models.TextField(null=True)),
                (
                    "deployment_report",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="details_report",
                        to="api.DeploymentsReport",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DisabledOptionalProductsOptions",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("jboss_eap", models.BooleanField(default=False)),
                ("jboss_fuse", models.BooleanField(default=False)),
                ("jboss_brms", models.BooleanField(default=False)),
                ("jboss_ws", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Entitlement",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256, null=True)),
                ("entitlement_id", models.CharField(max_length=256, null=True)),
                ("metadata", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="ExtendedProductSearchOptions",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("jboss_eap", models.BooleanField(default=False)),
                ("jboss_fuse", models.BooleanField(default=False)),
                ("jboss_brms", models.BooleanField(default=False)),
                ("jboss_ws", models.BooleanField(default=False)),
                ("search_directories", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="JobConnectionResult",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Job connection results",
            },
        ),
        migrations.CreateModel(
            name="JobInspectionResult",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Job inspection results",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("version", models.CharField(max_length=256, null=True)),
                (
                    "presence",
                    models.CharField(
                        choices=[
                            ("present", "Present"),
                            ("absent", "Absent"),
                            ("potential", "Potential"),
                            ("unknown", "Unknown"),
                        ],
                        max_length=10,
                    ),
                ),
                ("metadata", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="RawFact",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=1024)),
                ("value", models.TextField()),
            ],
            options={
                "verbose_name_plural": "Raw facts",
            },
        ),
        migrations.CreateModel(
            name="Scan",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64, unique=True)),
                (
                    "scan_type",
                    models.CharField(
                        choices=[("connect", "connect"), ("inspect", "inspect")],
                        default="inspect",
                        max_length=9,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Scans",
            },
        ),
        migrations.CreateModel(
            name="ScanJob",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "scan_type",
                    models.CharField(
                        choices=[
                            ("connect", "connect"),
                            ("inspect", "inspect"),
                            ("fingerprint", "fingerprint"),
                        ],
                        default="inspect",
                        max_length=12,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("created", "created"),
                            ("pending", "pending"),
                            ("running", "running"),
                            ("paused", "paused"),
                            ("completed", "completed"),
                            ("canceled", "canceled"),
                            ("failed", "failed"),
                        ],
                        default="created",
                        max_length=20,
                    ),
                ),
                (
                    "status_message",
                    models.TextField(default="Job is created.", null=True),
                ),
                ("report_id", models.IntegerField(null=True)),
                ("start_time", models.DateTimeField(null=True)),
                ("end_time", models.DateTimeField(null=True)),
                (
                    "connection_results",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.JobConnectionResult",
                    ),
                ),
                (
                    "details_report",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.DetailsReport",
                    ),
                ),
                (
                    "inspection_results",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.JobInspectionResult",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Scan jobs",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="ScanOptions",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("max_concurrency", models.PositiveIntegerField(default=50)),
                (
                    "disabled_optional_products",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.DisabledOptionalProductsOptions",
                    ),
                ),
                (
                    "enabled_extended_product_search",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.ExtendedProductSearchOptions",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ScanTask",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "scan_type",
                    models.CharField(
                        choices=[
                            ("connect", "connect"),
                            ("inspect", "inspect"),
                            ("fingerprint", "fingerprint"),
                        ],
                        max_length=12,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("created", "created"),
                            ("pending", "pending"),
                            ("running", "running"),
                            ("paused", "paused"),
                            ("completed", "completed"),
                            ("canceled", "canceled"),
                            ("failed", "failed"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                (
                    "status_message",
                    models.TextField(default="Task is pending.", null=True),
                ),
                ("systems_count", models.PositiveIntegerField(null=True)),
                ("systems_scanned", models.PositiveIntegerField(null=True)),
                ("systems_failed", models.PositiveIntegerField(null=True)),
                ("systems_unreachable", models.PositiveIntegerField(null=True)),
                ("sequence_number", models.PositiveIntegerField(default=0)),
                ("start_time", models.DateTimeField(null=True)),
                ("end_time", models.DateTimeField(null=True)),
            ],
            options={
                "verbose_name_plural": "Scan tasks",
                "ordering": ("sequence_number",),
            },
        ),
        migrations.CreateModel(
            name="ServerInformation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("global_identifier", models.CharField(max_length=36)),
            ],
        ),
        migrations.CreateModel(
            name="Source",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64, unique=True)),
                (
                    "source_type",
                    models.CharField(
                        choices=[
                            ("network", "network"),
                            ("vcenter", "vcenter"),
                            ("satellite", "satellite"),
                        ],
                        max_length=12,
                    ),
                ),
                ("port", models.IntegerField(null=True)),
                ("hosts", models.TextField()),
                ("exclude_hosts", models.TextField(null=True)),
                ("credentials", models.ManyToManyField(to="api.Credential")),
                (
                    "most_recent_connect_scan",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="api.ScanJob",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SourceOptions",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ssl_protocol",
                    models.CharField(
                        choices=[
                            ("SSLv23", "SSLv23"),
                            ("TLSv1", "TLSv1"),
                            ("TLSv1_1", "TLSv1_1"),
                            ("TLSv1_2", "TLSv1_2"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                ("ssl_cert_verify", models.NullBooleanField()),
                ("disable_ssl", models.NullBooleanField()),
                ("use_paramiko", models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="SystemConnectionResult",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("success", "success"),
                            ("failed", "failed"),
                            ("unreachable", "unreachable"),
                        ],
                        max_length=12,
                    ),
                ),
                (
                    "credential",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.Credential",
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.Source",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "System connection results",
            },
        ),
        migrations.CreateModel(
            name="SystemFingerprint",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256, null=True)),
                ("os_name", models.CharField(max_length=64)),
                ("os_release", models.CharField(max_length=128)),
                ("os_version", models.CharField(max_length=64, null=True)),
                (
                    "infrastructure_type",
                    models.CharField(
                        choices=[
                            ("bare_metal", "Bare Metal"),
                            ("virtualized", "Virtualized"),
                            ("unknown", "Unknown"),
                        ],
                        max_length=12,
                    ),
                ),
                ("mac_addresses", models.TextField(null=True)),
                ("ip_addresses", models.TextField(null=True)),
                ("cpu_count", models.PositiveIntegerField(null=True)),
                ("architecture", models.CharField(max_length=64, null=True)),
                ("bios_uuid", models.CharField(max_length=36, null=True)),
                ("subscription_manager_id", models.CharField(max_length=36, null=True)),
                ("cpu_socket_count", models.PositiveIntegerField(null=True)),
                ("cpu_core_count", models.FloatField(null=True)),
                ("system_creation_date", models.DateField(null=True)),
                ("system_last_checkin_date", models.DateField(null=True)),
                ("system_role", models.CharField(max_length=128, null=True)),
                ("system_addons", models.TextField(null=True)),
                (
                    "system_service_level_agreement",
                    models.CharField(max_length=128, null=True),
                ),
                ("system_usage_type", models.CharField(max_length=128, null=True)),
                ("insights_client_id", models.CharField(max_length=128, null=True)),
                ("virtualized_type", models.CharField(max_length=64, null=True)),
                ("vm_state", models.CharField(max_length=24, null=True)),
                ("vm_uuid", models.CharField(max_length=36, null=True)),
                ("vm_dns_name", models.CharField(max_length=256, null=True)),
                ("vm_host", models.CharField(max_length=128, null=True)),
                ("vm_host_socket_count", models.PositiveIntegerField(null=True)),
                ("vm_cluster", models.CharField(max_length=128, null=True)),
                ("vm_datacenter", models.CharField(max_length=128, null=True)),
                ("is_redhat", models.NullBooleanField()),
                ("redhat_certs", models.TextField(null=True)),
                ("redhat_package_count", models.PositiveIntegerField(null=True)),
                ("metadata", models.TextField()),
                ("sources", models.TextField()),
                (
                    "deployment_report",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="system_fingerprints",
                        to="api.DeploymentsReport",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SystemInspectionResult",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=1024)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("success", "success"),
                            ("failed", "failed"),
                            ("unreachable", "unreachable"),
                        ],
                        max_length=12,
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.Source",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "System inspection results",
            },
        ),
        migrations.CreateModel(
            name="TaskConnectionResult",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "job_connection_result",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="task_results",
                        to="api.JobConnectionResult",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Task connection results",
            },
        ),
        migrations.CreateModel(
            name="TaskInspectionResult",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "job_inspection_result",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="task_results",
                        to="api.JobInspectionResult",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Task inspection results",
            },
        ),
        migrations.AddField(
            model_name="systeminspectionresult",
            name="task_inspection_result",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="systems",
                to="api.TaskInspectionResult",
            ),
        ),
        migrations.AddField(
            model_name="systemconnectionresult",
            name="task_connection_result",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="systems",
                to="api.TaskConnectionResult",
            ),
        ),
        migrations.AddField(
            model_name="source",
            name="options",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.SourceOptions",
            ),
        ),
        migrations.AddField(
            model_name="scantask",
            name="connection_result",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.TaskConnectionResult",
            ),
        ),
        migrations.AddField(
            model_name="scantask",
            name="details_report",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.DetailsReport",
            ),
        ),
        migrations.AddField(
            model_name="scantask",
            name="inspection_result",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.TaskInspectionResult",
            ),
        ),
        migrations.AddField(
            model_name="scantask",
            name="job",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to="api.ScanJob",
            ),
        ),
        migrations.AddField(
            model_name="scantask",
            name="prerequisites",
            field=models.ManyToManyField(to="api.ScanTask"),
        ),
        migrations.AddField(
            model_name="scantask",
            name="source",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="api.Source"
            ),
        ),
        migrations.AddField(
            model_name="scanjob",
            name="options",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.ScanOptions",
            ),
        ),
        migrations.AddField(
            model_name="scanjob",
            name="scan",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="jobs",
                to="api.Scan",
            ),
        ),
        migrations.AddField(
            model_name="scanjob",
            name="sources",
            field=models.ManyToManyField(to="api.Source"),
        ),
        migrations.AddField(
            model_name="scan",
            name="most_recent_scanjob",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="api.ScanJob",
            ),
        ),
        migrations.AddField(
            model_name="scan",
            name="options",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.ScanOptions",
            ),
        ),
        migrations.AddField(
            model_name="scan",
            name="sources",
            field=models.ManyToManyField(to="api.Source"),
        ),
        migrations.AddField(
            model_name="rawfact",
            name="system_inspection_result",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="facts",
                to="api.SystemInspectionResult",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="fingerprint",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="api.SystemFingerprint",
            ),
        ),
        migrations.AddField(
            model_name="entitlement",
            name="fingerprint",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="entitlements",
                to="api.SystemFingerprint",
            ),
        ),
    ]
