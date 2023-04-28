jQuery( document ).ready(function( $ ) {

    // Botão de ver mais

    $(document).ready(function() {
        $('.ver-mais').click(function(e) {
          e.preventDefault(); // evita que o link seja seguido
          var description = $(this).prev('.description');
          description.slideToggle('fast', function() {
            if(description.is(":visible")){
              $(this).siblings('.ver-mais').text('Ver menos');
            } else {
              $(this).siblings('.ver-mais').text('Ver mais');
            }
          });
        });
      });


    // Navegação nas categorias

    // Seleciona a lista de categorias
    const categoriesList = document.querySelector('.categories ul');
    const items = document.querySelectorAll('.library-box');

    // Define o estilo "display: block" para todos os itens
    items.forEach(function (item) {
      item.style.display = 'block';
    });

    // Adiciona um evento de clique em cada link da lista de categorias
    categoriesList.addEventListener('click', function (event) {
      if (event.target.tagName === 'A') {
        event.preventDefault();

        // Obtém o nome da categoria clicada
        const category = event.target.dataset.category;

        // Filtra os itens que pertencem à categoria selecionada
        items.forEach(function (item) {
          if (item.id === category) {
            item.classList.add('show');
            item.classList.remove('hide');
            item.style.display = 'block';
          } else {
            item.classList.add('hide');
            item.classList.remove('show');
            item.style.display = 'none';
          }
        });
      }
    });

	"use strict";

        // Animação do Preloader

        $("#preloader").animate({
            'opacity': '0'
        }, 600, function(){
            setTimeout(function(){
                $("#preloader").css("visibility", "hidden").fadeOut();
            }, 300);
        });
        

        $(window).scroll(function() {
          var scroll = $(window).scrollTop();
          var box = $('.header-text').height();
          var header = $('header').height();

          if (scroll >= box - header) {
            $("header").addClass("background-header");
          } else {
            $("header").removeClass("background-header");
          }
        });

        if ($('.owl-clients').length) {
            $('.owl-clients').owlCarousel({
                loop: true,
                nav: false,
                dots: true,
                items: 1,
                margin: 30,
                autoplay: false,
                smartSpeed: 700,
                autoplayTimeout: 6000,
                responsive: {
                    0: {
                        items: 1,
                        margin: 0
                    },
                    460: {
                        items: 1,
                        margin: 0
                    },
                    576: {
                        items: 3,
                        margin: 20
                    },
                    992: {
                        items: 5,
                        margin: 30
                    }
                }
            });
        }

        if ($('.owl-banner').length) {
            $('.owl-banner').owlCarousel({
                loop: true,
                nav: true,
                dots: true,
                items: 3,
                margin: 10,
                autoplay: false,
                smartSpeed: 700,
                autoplayTimeout: 6000,
                responsive: {
                    0: {
                      items: 1,
                      margin: 0
                    },
                    460: {
                        items: 1,
                        margin: 0
                    },
                    576: {
                        items: 1,
                        margin: 10
                    },
                    992: {
                      items: 3,
                      margin: 10
                    }
                }
            });
        }
 
});
