#!/usr/bin/env python3
# click 是一个方便生成command line工具的python库
import click
import hashlib

def hashMD5(file):
    value = hashlib.md5(open(file, 'rb').read()).hexdigest()
    return value

def hashSHA1(file):
    value = hashlib.sha1(open(file, 'rb').read()).hexdigest()
    return value

def hashSHA256(file):
    value = hashlib.sha256(open(file, 'rb').read()).hexdigest()
    return value

def hashSHA512(file):
    value = hashlib.sha256(open(file, 'rb').read()).hexdigest()
    return value

# 以下是click的语法; @开头的叫decorator，以前没遇见过这个概念。
@click.command()
@click.argument('hash_type')
@click.argument('file')
# @click.argument('output')
@click.option('--output', help='如果在命令中增加--output=yes, 则校验结果会写入到output.txt')
def hashit(hash_type, file, output):

    hash_value = ''
    click.echo('使用 %s 进行校验' % hash_type)

    if hash_type.upper() == 'MD5':
        hash_value = hashMD5(file)
    elif hash_type.upper() == 'SHA1':
        hash_value = hashSHA1(file)
    elif hash_type.upper() == 'SHA256':
        hash_value = hashSHA256(file)
    elif hash_type.upper() == 'SHA512':
        hash_value = hashSHA512(file)

    if hash_value == '':
        click.echo('oops, 没有生成校验值，请尝试重新运行命令。')
    else:
        click.echo('校验值为 %s' % hash_value)

    if output and output.upper() == 'YES':
        f = open('output.txt', 'w')
        f.write('文件 %s 的 %s 校验值为:\n' % (file, hash_type))
        f.write(hash_value + '\n')
        f.close()
        click.echo('校验值已经写入output.txt')

if __name__ == '__main__':
    hashit()
