var gulp = require('gulp')
var plugins = require('gulp-load-plugins')()
var path = require('path')

gulp.task('clean', () => {
	let sources = ['**/bower_components', '**/*.zip', '!node_modules/**/*.zip']
	return gulp
		.src(sources, {read: false})
		.pipe(plugins.rimraf())
})

gulp.task('bower', ['clean'], () => {
	let sources = ['**/bower.json', '!node_modules/**/bower.json']
	return gulp
		.src(sources, { read: false })
		.pipe(plugins.shell([
			'cd <%= getPath(file.path) %> && bower install -F'
		], {
			templateData: {
				getPath: x => '"' + path.dirname(x) + '"'
			}
		}))
})

gulp.task('zip', () => {
	let sources = ['!node_modules/**', '!**/bower_components/**', '**/bower.json']

	return gulp
		.src(sources, { read: false })
		.pipe(plugins.shell([
			'echo <%= file.path %>',
			'cd <%= getPath(file.path) %> && zip -9 -r file.zip .'
		], {
			templateData: {
				getPath: x => '"' + path.dirname(x) + '"'
			}
		}))
		.on('error', e => plugins.util.log)
})
