from setuptools import find_packages, setup

package_name = 'smart_diffbot_safety'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Manthan',
    maintainer_email='113732468+NeverGotRickRolled@users.noreply.github.com',
    description='Monitoring-only front-sector LaserScan obstacle monitor.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'scan_safety_monitor = smart_diffbot_safety.scan_safety_monitor:main',
        ],
    },
)
