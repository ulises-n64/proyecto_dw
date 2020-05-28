#post_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime
# Create your views here.
posts = [
	{
		'title': 'Primer campeonato',
		'user': {
			'name': 'Michel Jordan',
			'picture': 'data:image/jpeg;base64,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'
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'photo': 'https://naciondeportes.com/wp-content/uploads/2018/02/Los-mejores-momentos-en-la-carrera-de-Michael-Jordan.jpg',
	},
	{
		'title': 'Dia del niño',
		'user': {
			'name': 'Bruno Mars',
			'picture': 'data:image/jpeg;base64,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'
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'photo': 'https://childhoodbiography.com/wp-content/uploads/2019/09/Bruno-Mars-Childhood-Story-Plus-Untold-Biography-Facts-696x467.jpg',
	},
	{
		'title': 'Yo soy Superman',
		'user': {
			'name': 'Henry Cavill',
			'picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSqe9zv-44vSv39ueJ79rDmeJX4yaskTxSALsvIMuxs5cmI1u4C&usqp=CAU'
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'photo': 'https://spoiler.bolavip.com/__export/1588715726669/sites/bolavip/img/2020/05/05/henry_cavill_crop1588714409928.jpg_1693159006.jpg',
	},
	{
		'title': 'Super bowl',
		'user': {
			'name': 'Shakira',
			'picture': 'https://mui.today/__export/1586382479545/sites/mui/img/2020/04/08/shakira-kmo2e.jpg_55670814.jpg'
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'photo': 'https://www.eluniverso.com/sites/default/files/styles/powgallery_1280/public/fotos/2020/03/218956_0.jpg?itok=3Wqd5uzp',
	}
]
@login_required
def list_posts(request):
	# """list existing posts"""
	# content=[]
	# for post in posts:
	# 	content.append("""
	# 	<p><strong>{name}</strong></p>
	# 	<p><small>{user} - <i>{timestamp}</i></small></p>
	# 	<figure><img src="{picture}"/></figure>
	# 	""".format(**post))
	# return HttpResponse('<br>'.join(content))
	return render(request,'posts/feed2.html', {'posts':posts})
