function gitu(){
    cd
    cd Desktop/Python/
    mkdir $1
    cd $1
    python3 main.py $1
    touch README.md
    git init
    git add .
    git commit -m "initial commit"
    git push -u origin master
    code .
}