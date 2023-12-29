from authors.forms.recipe_form import AuthorRecipeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from recipes.models import Recipe


@method_decorator(
    login_required(login_url='authors:login', redirect_field_name='next'),
    name='dispatch'
)
class DashboardRecipe(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self, *args, **kwargs):
        return super().setup(*args, **kwargs)

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    # metodo para obter a receita pelo id
    def get_recipe(self, id=None):
        # para inicializar
        recipe = None

        # caso tenha id
        if id is not None:
            # recupera a receita filtrando por  id,
            # usuario logado e se nao esta publicado
            recipe = Recipe.objects.filter(
                is_published=False,
                author=self.request.user,
                pk=id,
                # obtendo a primeira
            ).first()

            # caso nao tenha receita, 404
            if not recipe:
                raise Http404()

        # retorna a receita que vai ser editada
        return recipe

    #  metodo para renderizar a receita no html
    def render_recipe(self, form):
        return render(
            # renderiza a pagina e passa o formulario como contexto
            self.request,
            'authors/pages/dashboard_recipe.html',
            context={
                'form': form
            }
        )

    # metodo get para mostrar o formulario na tela ja existente
    # recebe a requisicao e o id da receita
    def get(self, request, id=None):
        # recipe recebe o retorno da funcao acima, que obtem a receita
        recipe = self.get_recipe(id)
        # essa recipe é passada como instancia para ser gerado o form
        # sem essa instancia, o form apareceria vazio
        form = AuthorRecipeForm(instance=recipe)
        # renderiza esse form no html
        return self.render_recipe(form)

    def post(self, request, id=None):
        # recebe a receita chamando a funcao criado com o id
        recipe = self.get_recipe(id)

        # form recebe dados do POST com a instancia recebida
        form = AuthorRecipeForm(
            data=request.POST or None,
            files=request.FILES or None,
            instance=recipe
        )

        # Esse trecho valida o formulario antes de salv=a-lo
        if form.is_valid():
            recipe = form.save(commit=False)
            # aqui ele garante que todas as informacoes antes de salvar
            recipe.author = request.user
            recipe.preparation_steps_is_html = False
            recipe.is_published = False
            # salva no bd
            recipe.save()
            # mostra a flash message na tela
            messages.success(request, 'Sua receita foi salva com sucesso!')
            # redireciona para a própria página
            return redirect(
                reverse(
                    'authors:dashboard_recipe_edit', args=(
                        recipe.id,
                    )
                )
            )

        # retorna a renderizacao do html após o processo
        return self.render_recipe(form)
