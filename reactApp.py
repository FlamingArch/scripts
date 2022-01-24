import os
import sys

proj_name = sys.argv[1]

print(proj_name)

# region Create Project Directory
os.chdir("/Users/flamingarch/Developer")
os.mkdir(proj_name)
os.chdir(proj_name)
# endregion


init_app = [
    "npx create-react-app .",
    "npm install -D tailwindcss postcss autoprefixer",
    "npx tailwindcss init -p",
]

for line in init_app:
    os.system(line)


tailwind_config = """
module.exports = {
    content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    ],
    theme: {
    extend: {},
    },
    plugins: [],
}
"""

with open("tailwind.config.js", "w") as stream:
    stream.write(tailwind_config)


remove_src_files = [
    "App.css", "App.test.js", "App.js", "index.css", "index.js",
    "logo.svg", "reportWebVitals.js", "setupTests.js",
]

for file in remove_src_files:
    os.remove("./src/" + file)

app_js = """
import React from "react";

const App = () => {
  return (
    <div className="grid place-content-center w-screen h-screen  text-xl">
      <h1 className="text-red-500 pb-2 text-6xl font-extralight">
        Hello, world!
      </h1>
      <p>
        Created New <span className="text-blue-500 ">React</span> App with:
      </p>
      <ul className="list-disc pl-8">
        <li>TailwindCSS</li>
        <li>Hero Icons</li>
        <li>Framer Motion</li>
        <li>Lodash</li>
        <li>JQuery</li>
      </ul>
    </div>
  );
};

export default App
"""

with open('./src/App.js', "w") as stream:
    stream.write(app_js)


index_css = "@tailwind base;\n@tailwind components;\n@tailwind utilities;\n"

with open("./src/index.css", "w") as stream:
    stream.write(index_css)

index_js = """
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App'

ReactDOM.render(
  <React.StrictMode>
    <App/>
  </React.StrictMode>,
  document.getElementById('root')
);
"""

with open("./src/index.js", "w") as stream:
    stream.write(index_js)


npm_installs = ["@heroicons/react", "framer-motion", "lodash", "jquery"]

for package in npm_installs:
    os.system("npm install " + package)


os.remove("./public/index.html")

index_html = f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta name="description" content="© Harsh Chaturvedi" />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    <title>{proj_name}</title>
  </head>""" + """
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
    <script>
      if ("serviceWorker" in navigator) {
        window.addEventListener("load", function () {
          navigator.serviceWorker
            .register("worker.js")
            .then(
              function (registration) {
                console.log(
                  "Worker registration successful",
                  registration.scope
                );
              },
              function (err) {
                console.log("Worker registration failed", err);
              }
            )
            .catch(function (err) {
              console.log(err);
            });
        });
      } else {
        console.log("Service Worker is not supported by browser.");
      }
    </script>
  </body>
</html>
"""

with open("./public/index.html", "w") as stream:
    stream.write(index_html)

worker_js = """
var CACHE_NAME = "pwa-task-manager";
var urlsToCache = ["/", "/completed"];

// Install a service worker
self.addEventListener("install", (event) => {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME).then(function (cache) {
      console.log("Opened cache");
      return cache.addAll(urlsToCache);
    })
  );
});

// Cache and return requests
self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then(function (response) {
      // Cache hit - return response
      if (response) {
        return response;
      }
      return fetch(event.request);
    })
  );
});

// Update a service worker
self.addEventListener("activate", (event) => {
  var cacheWhitelist = ["pwa-task-manager"];
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
"""

with open("./public/worker.js", "w") as stream:
    stream.write(worker_js)


os.system("git add .")
os.system("git commit -m 'Setup Project Files, added TailwindCSS, HeroIcons, Framer Motion, Lodash, JQuery'")

os.system("github .")

os.system("code .")
