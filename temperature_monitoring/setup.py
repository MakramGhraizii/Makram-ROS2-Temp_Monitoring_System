from setuptools import find_packages, setup
from glob import glob
import os
package_name = 'temperature_monitoring'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name),glob('launch/*launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='makramghraizi',
    maintainer_email='makramghraizi14@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'temperature_publisher = temperature_monitoring.temperature_publisher:main',
            'threshold_subscriber = temperature_monitoring.threshold_subscriber:main',
            'alert_publisher = temperature_monitoring.alert_publisher:main',
        ],
    },
)
