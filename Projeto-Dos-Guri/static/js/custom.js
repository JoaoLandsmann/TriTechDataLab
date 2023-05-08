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

    // Seleciona todos os itens com a classe "library-box"
    const items = document.querySelectorAll('.library-box');

    // Exibe todos os itens
    items.forEach(function (item) {
      item.style.display = 'block';
    });

    // Obtém o valor do parâmetro "id" da URL
    const urlParams = new URLSearchParams(window.location.search);
    const categoryId = urlParams.get('id');

    // Filtra os itens que pertencem à categoria selecionada
    if (categoryId) {
      items.forEach(function (item) {
        if (item.id === categoryId) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    }

    const links = document.querySelectorAll('.content ul li a');
    links.forEach(function(link) {
      link.addEventListener('click', function(event) {
        event.preventDefault();
        const categoryId = this.getAttribute('href').replace('#', '');
        items.forEach(function (item) {
          if (item.id === categoryId || categoryId === 'all') {
            item.style.display = 'block';
          } else {
            item.style.display = 'none';
          }
        });
      });
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
