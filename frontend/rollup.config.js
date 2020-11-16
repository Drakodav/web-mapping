import resolve from '@rollup/plugin-node-resolve';
import babel from '@rollup/plugin-babel'
import typescript from '@rollup/plugin-typescript';
import workbox from 'rollup-plugin-workbox-build';
import { uglify } from "rollup-plugin-uglify";

export default {
  input: 'index.ts',
  output: {
    // file: 'dist/static/bundle.js',
    dir: 'dist/static/',
    format: 'iife',
    name: 'bundle',
    sourcemap: true,
    // globals: {}
  },
  plugins: [
    typescript(),
    uglify(),
    resolve({
      // pass custom options to the resolve plugin
      customResolveOptions: {
        moduleDirectory: './node_modules'
      }
    }),
    babel({
      exclude: './node_modules/**', // only transpile our source code
      babelHelpers: 'bundled'
    }),
    workbox({
      mode: 'generateSW', // or 'injectManifest'
      options: {
        swDest: 'dist/service-worker.js',
        globDirectory: 'dist',
      },
      exclude: [/\.map$/, /static/]
    }),
  ],
  external: ['workbox-sw'],
};
