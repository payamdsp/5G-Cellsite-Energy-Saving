import boto3

def create_secure_emr_cluster():
    emr = boto3.client('emr')
    response = emr.run_job_flow(
        Name="CellsiteEnergyEMR",
        ReleaseLabel="emr-6.13.0",
        Instances={
            'InstanceGroups': [
                {'Name': "Master", 'Market': 'SPOT', 'InstanceRole': 'MASTER', 'InstanceType': 'm5.xlarge', 'InstanceCount': 1},
                {'Name': "Core",   'Market': 'SPOT', 'InstanceRole': 'CORE',   'InstanceType': 'm5.xlarge', 'InstanceCount': 4}
            ],
            'Ec2KeyName': 'YOUR_KEY_PAIR',
            'KeepJobFlowAliveWhenNoSteps': False,
            'TerminationProtected': False,
            'Ec2SubnetId': 'YOUR_SUBNET_ID'
        },
        SecurityConfiguration='YOUR_SECURITY_CONF',
        Applications=[{'Name': 'Spark'}],
        JobFlowRole='EMR_EC2_DefaultRole',
        ServiceRole='EMR_DefaultRole',
        VisibleToAllUsers=True,
        AutoScalingRole='EMR_AutoScaling_DefaultRole'
    )
    print(f"Started EMR cluster with id: {response['JobFlowId']}")