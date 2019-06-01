from setuptools import setup, find_packages

setup(
    name='cabot-discoball',
    packages=find_packages(),
    version='0.1.0',
    license='MIT',
    description='The caBot Discoball Module.',
    author='Joseph Hanna',
    author_email='josephhanna@centennialarts.com',
    url='https://github.com/centennialarts/cabot-discoball',
    download_url='https://github.com/centennialarts/cabot-discoball/archive/master.zip',
    keywords=['Chatbot', 'Discoball'],
    install_requires=[
        'cabot-core'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)