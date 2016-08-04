# -*- coding=utf-8 -*-


import urllib2
from BeautifulSoup import BeautifulSoup as bs3
import json
import codecs

#字符检测，用来检测其真实的编码格式
import chardet

#save content to file
def save_to_file(filename, content):
	f = open(filename, 'w+')
	assert(f)
	f.write(content)
	f.close()
	
def parse_key_link(content):
	old_code_name = chardet.detect(content)['encoding']
	print('old_code_name[key_link]=%s' % (old_code_name,))
	
	js = json.loads(content.decode(old_code_name))
	
	for i in js['result']['items']:
		print('name=%s, link=%s' % (i['name'].encode(old_code_name),i['link'].encode(old_code_name)))

def parse_config(content):
	old_code_name = chardet.detect(content)['encoding']
	print('old_code_name[config]=%s' % (old_code_name,))
	
	js = json.loads(content.decode(old_code_name))
	
	for i in js['result']['paramtypeitems']:
		print('name=%s' % (i['name'].encode(old_code_name),))
		i1 = i['paramitems']
		for j in i1:
			print('  name=%s' % (j['name'].encode(old_code_name),))
			j1 = j['valueitems']
			for k in j1:
				print('    specid=%d,value=%s' % (k['specid'],k['value'].encode(old_code_name)))
	
def parse_option(content):
	old_code_name = chardet.detect(content)['encoding']
	print('old_code_name[option]=%s' % (old_code_name,))
	
	js = json.loads(content.decode(old_code_name))
	
	for i in js['result']['configtypeitems']:
		print('name=%s' % (i['name'].encode(old_code_name),))
		i1 = i['configitems']
		for j in i1:
			print('  name=%s' % (j['name'].encode(old_code_name),))
			j1 = j['valueitems']
			for k in j1:
				print('    specid=%d,value=%s' % (k['specid'],k['value'].encode(old_code_name)))
	
def parse_color(content):
	old_code_name = chardet.detect(content)['encoding']
	print('old_code_name[color]=%s' % (old_code_name,))
	
	js = json.loads(content.decode(old_code_name))
	
	for i in js['result']['specitems']:
		print('specid=%d' % (i['specid'],))
		i1 = i['coloritems']
		for j in i1:
			print('  id=%d,name=%s,value=%s,picnum=%d' % \
			(j['id'],j['name'].encode(old_code_name),j['value'].encode(old_code_name),j['picnum']))
	
def parse_innerColor(content):
	old_code_name = chardet.detect(content)['encoding']
	print('old_code_name[innerColor]=%s' % (old_code_name,))
	
	js = json.loads(content.decode(old_code_name))
	
	for i in js['result']['specitems']:
		print('specid=%d' % (i['specid'],))
		i1 = i['coloritems']
		for j in i1:
			j1 = j['values']
			for k in j1:
				print('  id=%d,name=%s,value=%s,picnum=%d' % \
				(j['id'],j['name'].encode(old_code_name),k.encode(old_code_name),j['picnum']))
	
def parse_json_data(content):
	name_list = ['keyLink', 'config', 'option','color', 'innerColor']
	
	parse_list = [parse_key_link, parse_config, parse_option, parse_color, parse_innerColor]
	assert(len(content) == len(parse_list))
	for i in range(len(content)):
		parse_list[i](content[i])

def parse_content(content):
	#content是GB2312的编码
	soup = bs3(content)
	
	key_text = 'var levelId'
	elem_lib = soup.find('script', text=lambda(x):key_text in x)
	
	#str_script是utf-8的编码
	str_script = str(elem_lib.string)
	
	#print(chardet.detect(str_script))
	
	#由于命令行是cp936 GBK的编码，如果编码不符合无法打印
	strGBK = str_script.decode('utf-8').encode('gb2312')
	#print(strGBK)
	
	#移除html的转义字符&nbsp;
	strGBK = strGBK.replace('&nbsp;','')
	
	d = strGBK.splitlines()
	list_data = []
	
	for i in d:
		if i.isspace():
			continue
		
		#过滤不需要的变量
		if len(i) < 100:
			continue
		
		#取出json数据
		idx = i.find('{')
		if idx == -1:
			continue
		
		#移除最后的;
		k = i[idx:-1]
		list_data.append(k)
	
	parse_json_data(list_data)
	
def crawler_4_autohome():
	autohome_url = 'http://car.autohome.com.cn/config/series/657.html'
	
	#uft-8
	content = urllib2.urlopen(url=autohome_url).read()
	#print(chardet.detect(content))
	parse_content(content)
	
	
if __name__ == '__main__':
	crawler_4_autohome()
	
	
	
	
	
	