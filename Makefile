src	=	$(wildcard SrcGame/*.py main.py)

name  =		chessGame

all: $(name)

$(name):	$(src)
	    cp main.py $(name)
		chmod +x $(name)

clean:
	    rm -f $(name)

auteur:
	    echo $(user) > auteur

re:		clean $(name)
