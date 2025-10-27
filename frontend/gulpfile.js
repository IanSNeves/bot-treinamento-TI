const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const sourcemaps = require('gulp-sourcemaps');

function compilaSass() {
    return gulp.src('src/styles/**/*.scss')
    .pipe(sourcemaps.init())
    .pipe(sass({outputStyle: 'compressed'}))
    .pipe(sourcemaps.write('./maps'))
    .pipe(gulp.dest('../backend/static/css'));
}

function monitoraSass() {
    gulp.watch('src/styles/**/*.scss', { ignoreInitial: false }, compilaSass);
}


exports.default = monitoraSass;
exports.compilaSass = compilaSass;


compilaSass();