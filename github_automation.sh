function gitu(){
    cd ~/Desktop/Python/GitHub\ Automation/
    python3 main.py $1
    cd ..
    mkdir $1
    cd $1
    virtualenv env
    source ./env/bin/activate
    touch main.py
    git init
    git remote add origin git@github.com:ShahadilMunawir/$1.git
    git add .
    git commit -m "initial commit"
    git push -u origin master
    code .
}