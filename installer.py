from setuptools import setup, find_packages

setup(name='androhack',
      version='8.0.0',
      description=(
          ' androhack tool is a sophisticated post-exploitation tool specifically designed for Android devices. It utilizes the Android Debug Bridge (ADB) protocol, which is a versatile command-line tool that allows communication with a device. By exploiting ADB, Ghost Framework provides an avenue for remotely accessing and controlling an Android device, even if the device is not rooted.'
      ),
      url='https://github.com/DarkKnightGeeky/AndroHack.git',
      author='CyberLord',
      author_email='darkknightgeeky@gmail.com',
      license='MIT',
      python_requires='>=3.7.0',
      packages=find_packages(),
      include_package_data=True,
      entry_points={
          "console_scripts": [
              "androhack = androhack:cli"
          ]
      },
      install_requires=[
          'adb-shell',
          'pex @ git+https://github.com/EntySec/Pex',
          'badges @ git+https://github.com/EntySec/Badges',
          'colorscript @ git+https://github.com/EntySec/ColorScript'
      ],
      zip_safe=False
      )
