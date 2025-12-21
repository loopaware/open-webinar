<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import Header from '@/components/Header.vue'
import Hero from '@/components/Hero.vue'
import BackgroundScene from '@/components/BackgroundScene.vue'
import Speakers from '@/components/Speakers.vue'
import Agenda from '@/components/Agenda.vue'
import RegisterForm from '@/components/RegisterForm.vue'
import { Github, Twitter, Linkedin, Mail } from 'lucide-vue-next'

const props = defineProps<{
  speakers: any[]
  agenda: any[]
  settings: Record<string, string>
  new_attendee?: any
}>()

const event_date = computed(() => props.settings.event_date || '2025-12-24')
const site_title = computed(() => props.settings.site_title || 'OpenWebinar')

const countdown = ref('')

const updateCountdown = () => {
  const targetDate = new Date(`${event_date.value} 10:00:00`).getTime()
  const now = new Date().getTime()
  const distance = targetDate - now

  if (distance < 0) {
    countdown.value = "THE UNVEILING HAS BEGUN"
  } else {
    const days = Math.floor(distance / (1000 * 60 * 60 * 24))
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60))
    const seconds = Math.floor((distance % (1000 * 60)) / 1000)
    countdown.value = `${days}D ${hours}H ${minutes}M ${seconds}S`
  }
}

onMounted(() => {
  updateCountdown()
  setInterval(updateCountdown, 1000)
  document.title = site_title.value
})
</script>

<template>
  <div class="min-h-screen bg-brand-obsidian text-brand-bone selection:bg-brand-gold selection:text-brand-obsidian overflow-x-hidden">
    <BackgroundScene />
    <Header :site_title="site_title" />

    <main class="relative z-10">
      <Hero :countdown="countdown" :settings="settings" />
      
      <div class="relative">
        <div class="absolute inset-0 bg-gradient-to-b from-transparent via-brand-mycelium/5 to-transparent pointer-events-none"></div>
        <Speakers :speakers="speakers" />
      </div>

      <Agenda :items="agenda" />

      <RegisterForm :new_attendee="new_attendee" :event_date="event_date" />
    </main>

    <footer class="bg-black border-t border-white/5 text-white pt-32 pb-16 px-8 relative z-10">
      <div class="max-w-7xl mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-20 mb-24">
          <div class="col-span-1 md:col-span-2">
            <div class="flex items-center gap-4 mb-10 group cursor-pointer">
              <div class="w-12 h-12 bg-brand-gold/10 rounded-2xl flex items-center justify-center border border-brand-gold/20 group-hover:rotate-12 transition-transform">
                <img src="/img/logo.png" alt="Logo" class="w-8 h-8">
              </div>
              <span class="text-3xl font-black tracking-tighter uppercase">{{ site_title }}</span>
            </div>
            <p class="text-brand-mist/30 leading-relaxed max-w-md mb-12 text-lg font-light">
              {{ settings.footer_description || 'Empowering the next generation of digital connections through immersive webinar experiences.' }}
            </p>
            <div class="flex gap-6">
              <a href="#" class="w-12 h-12 rounded-2xl bg-white/5 hover:bg-brand-gold/20 flex items-center justify-center transition-all hover:-translate-y-1"><Twitter class="w-5 h-5" /></a>
              <a href="#" class="w-12 h-12 rounded-2xl bg-white/5 hover:bg-brand-gold/20 flex items-center justify-center transition-all hover:-translate-y-1"><Linkedin class="w-5 h-5" /></a>
              <a href="#" class="w-12 h-12 rounded-2xl bg-white/5 hover:bg-brand-gold/20 flex items-center justify-center transition-all hover:-translate-y-1"><Github class="w-5 h-5" /></a>
            </div>
          </div>
          
          <div>
            <h4 class="font-black text-[10px] tracking-[0.5em] mb-10 text-brand-gold uppercase">The Access</h4>
            <ul class="space-y-6 text-brand-mist/40 font-bold text-sm uppercase">
              <li><a href="#about" class="hover:text-brand-gold transition-colors">Origins</a></li>
              <li><a href="#speakers" class="hover:text-brand-gold transition-colors">Visionaries</a></li>
              <li><a href="#agenda" class="hover:text-brand-gold transition-colors">The Map</a></li>
              <li><a href="#register" class="hover:text-brand-gold transition-colors">Entry Protocol</a></li>
            </ul>
          </div>

          <div>
            <h4 class="font-black text-[10px] tracking-[0.5em] mb-10 text-brand-gold uppercase">Coordinates</h4>
            <ul class="space-y-6 text-brand-mist/40 text-sm">
              <li class="flex items-center gap-4 group cursor-pointer font-bold uppercase"><Mail class="w-4 h-4 group-hover:text-brand-gold transition-colors" /> contact@openwebinar.io</li>
              <li class="leading-loose font-light">OpenWebinar Headquarters<br>Digital Space, Scandinavia</li>
            </ul>
          </div>
        </div>
        
        <div class="pt-12 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-8 text-[10px] font-black tracking-[0.2em] text-white/20 uppercase">
          <p>&copy; 2025 {{ site_title.toUpperCase() }}. ALL RIGHTS RESERVED.</p>
          <div class="flex gap-10">
            <a href="#" class="hover:text-white transition-colors">Privacy Protocol</a>
            <a href="#" class="hover:text-white transition-colors">Terms of Existence</a>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<style>
html {
  scroll-behavior: smooth;
}
::selection {
  background: #fbbf24;
  color: #050a05;
}
</style>