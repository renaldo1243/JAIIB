// RBWM Prep service worker: app works offline; question/notes files refresh when online.
const CACHE='jaiib-prep-v2';
const CORE=['./','./index.html','./bank.json','./notes.json','./bank_ieifs.json','./notes_ieifs.json','./manifest.json','./icon-192.png','./icon-512.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{
  const req=e.request; if(req.method!=='GET') return;
  const url=new URL(req.url);
  const same=url.origin===location.origin;
  if(same){ // network first, fall back to cache (so new questions arrive when online)
    e.respondWith(fetch(req).then(r=>{const c=r.clone(); caches.open(CACHE).then(ca=>ca.put(req,c)); return r}).catch(()=>caches.match(req,{ignoreSearch:true}).then(r=>r||caches.match('./index.html'))));
  } else if(/fonts\.(googleapis|gstatic)\.com$/.test(url.hostname)){ // cache fonts
    e.respondWith(caches.match(req).then(r=>r||fetch(req).then(n=>{const c=n.clone(); caches.open(CACHE).then(ca=>ca.put(req,c)); return n})));
  }
});
