from setuptools import setup, find_packages

setup(
    name='print_formatted_tensor',
    version='0.1',
    packages=find_packages(),
    description='Utility for formatted printing of PyTorch tensors',
    author='Hayato Hongo',
    author_email='hongo.hayato.6281k@gmail.com',
    url='https://github.com/HayatoHongo/print_formatted_tensor',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'torch',
    ],
)