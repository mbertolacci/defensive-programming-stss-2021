rmarkdown::render(
  'slides.Rmd',
  output_file = 'docs/index.html',
  output_options = list(
    self_contained = TRUE,
    reveal_plugins = c()
  )
)
