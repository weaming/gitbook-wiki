init:
	pip install -r requirements.txt

build:
	python gen_summary.py

serve: build
	gitbook serve

publish: build
	git add -A
	git commit -m "`date '+%Y/%m/%d %H:%M'`"
	git push

clean:
	rm -rf _book

.PHONY: init build serve publish clean
