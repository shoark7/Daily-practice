"""Create .gitignore file with Python

This is a program that builds .gitignore with gitignore.io's APIs.
(https://www.gitignore.io/)

In its github(https://github.com/joeblau/gitignore.io) they support apis through shells,
but I wanted to implement it through Python script.

Start Date: 2018/03/09
End   Date: 2018/?????
"""

import argparse
import datetime
import re
import requests
import string


URL_PREFIX = 'https://www.gitignore.io/api/'
TOTAL_LIST = 'actionscript,ada,agda,android,appceleratortitanium,appcode,archives,
archlinuxpackages,autotools,bancha,basercms,bower,bricxcc,c,c++,cakephp,
cfwheels,chefcookbook,clojure,cloud9,cmake,codeigniter,codekit,commonlisp,
compass,composer,concrete5,coq,cvs,dart,darteditor,delphi,django,dotsettings,
dreamweaver,drupal,eagle,eclipse,elasticbeanstalk,elisp,elixir,emacs,ensime,
episerver,erlang,espresso,expressionengine,fancy,finale,flexbuilder,forcedotcom,
freepascal,fuelphp,gcov,go,gradle,grails,gwt,haskell,intellij,java,jboss,jekyll,
jetbrains,joe,joomla,justcode,jython,kate,kdevelop4,kohana,komodoedit,laravel,
latex,lazarus,leiningen,lemonstand,lilypond,linux,lithium,magento,matlab,maven,
mercurial,meteor,modelsim,monodevelop,nanoc,netbeans,node,notepadpp,objective-c,
ocaml,opa,opencart,openfoam,oracleforms,osx,perl,ph7cms,phpstorm,playframework,
plone,prestashop,processing,pycharm,python,qooxdoo,qt,quartus2,r,rails,redcar,
rhodesrhomobile,ros,ruby,rubymine,rubymotion,sass,sbt,scala,scrivener,sdcc,
seamgen,senchatouch,silverstripe,sketchup,stella,sublimetext,sugarcrm,svn,
symfony,symfony2,symphonycms,tags,target3001,tarmainstallmate,tasm,tex,textmate,
textpattern,turbogears2,typo3,unity,vagrant,vim,virtualenv,visualstudio,vvvv,
waf,wakanda,webmethods,webstorm,windows,wordpress,xamarinstudio,xcode,xilinxise,
yeoman,yii,zendframework'


# get user input
langs = input().strip().lower()


# langs re validation
pattern = re.compile(r'([abcdefghijklmnopqrstuvwxyz]+,?)+')
if not pattern.fullmatch(lnags):
    raise ValueError('Langauges are not in right forms. Must be "lang[+,+lang]", without spaces')


# requests & response
lang_list = langs.split(',')
url = URL_PREFIX + langs
text = requests.get(url).text


# write to a file
with open('./.gitignore') as fd:
    fd.wirte(text)
