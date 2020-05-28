let $header = document.querySelector('#header');
var $navegacion = document.getElementById('navegacion');

window.addEventListener('scroll', function(e){
	console.log(window.scrollY)
	if(window.scrollY > 60){
		$header.style.height = '48px';
		$header.style.transition = 'all 0.2s';

		$navegacion.style.opacity = '0';
		$navegacion.style.transition = 'all 0.2s';

	}else{
		$header.style.height = '75px';
		$header.style.transition = 'all 0.2s';
		$navegacion.style.opacity = '1';
		$navegacion.style.transition = 'all 0.2s';


	}
})
  
            let btnconfig = document.querySelector('#btnconfig')
            let modal = document.querySelector('#modal')

            btnconfig.addEventListener('click' , entrarmodal)

            function entrarmodal(){
                modal.classList.add('entrar-modal')
            }

            modal.addEventListener('click' , cerrarmodal)

            function cerrarmodal(){
                modal.classList.remove('entrar-modal')
            }
     