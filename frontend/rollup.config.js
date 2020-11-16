import workbox from 'rollup-plugin-workbox-build';
import typescript from 'rollup-plugin-typescript';
import { uglify } from "rollup-plugin-uglify";
import resolve from '@rollup/plugin-node-resolve';
import babel from 'rollup-plugin-babel'

export default {
  input: 'index.ts',
  output: {
    file: 'dist/static/bundle.js',
    format: 'iife',
    name: 'bundle',
    publicPath: '/',
    globals: {
      'workbox-routing': 'workboxRouting',
      'workbox-strategies': 'workboxStrategies',
      'workbox-expiration': 'workboxExpiration'
    }
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
