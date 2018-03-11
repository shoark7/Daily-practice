"""Create .gitignore file with Python

This is a program that builds .gitignore with gitignore.io's APIs.
(https://www.gitignore.io/)

In its github(https://github.com/joeblau/gitignore.io) they support apis through shells,
but I wanted to implement it through Python script.

Start Date: 2018/03/09
End   Date: 2018/03/10
"""

import datetime
import re
import requests


TODAY = datetime.datetime.today()
URL_PREFIX = 'https://www.gitignore.io/api/'
TOTAL_LIST = """actionscript,ada,agda,android,appceleratortitanium,appcode,archives,
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
yeoman,yii,zendframework"""


def create_gitignore(stream='./.gitignore'):
    """Create .gitignore file

    This function creates .gitignore file with user input of frameworks.
    Current directory is the default location.

    It gets user input as a string of frameworks concatenated with ',' without spaces.
    And then parses the string using ',' as a delimiter and sends a http request.

    This prints out which langs were valid or not.
    """
    ori_langs = input().strip()
    lower_langs = ori_langs.lower()


    pattern = re.compile(r'([abcdefghijklmnopqrstuvwxyz]+,?)+')
    if not pattern.fullmatch(lower_langs):
        raise ValueError('Langauges are not in right forms. Must be "lang[+,+lang]", without spaces')

    lower_langs = lower_langs.split(',')
    ori_langs = ori_langs.split(',')


    valid_langs = [l for l in lower_langs if l in TOTAL_LIST]
    unvalid_langs = [l for l in lower_langs if l not in TOTAL_LIST]
    url = URL_PREFIX + ','.join(valid_langs)
    text = requests.get(url).text
    if not valid_langs:
        print("I cannot recognize any of your words... Program exited")
        return None


    with open(stream, 'w') as fd:
        fd.write(text)
        fd.write('# Made at {:4d}/{:02d}/{:02d}'.format(TODAY.year, TODAY.month, TODAY.day))


    print('\nSuccessfully created with {} languages:\n'.format(len(valid_langs)))
    for lang in valid_langs:
        print('\t{lang}'.format(
            lang=ori_langs[lower_langs.index(lang)]
        ))
    print('\n')

    if unvalid_langs:
        print('############# Error #############')
        print("Couldn't get the message of these:\n")
        for lang in unvalid_langs:
            print('\t{lang}'.format(
                lang=ori_langs[lower_langs.index(lang)]
            ))
        print("\nMaybe you need another shot after correcting typos")
        print('\n#################################')


if __name__ == '__main__':
    create_gitignore()
