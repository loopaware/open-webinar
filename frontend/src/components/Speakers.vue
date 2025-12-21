<script setup lang="ts">
defineProps<{
  speakers: any[]
}>()
</script>

<template>
  <section id="speakers" class="py-32 px-6 bg-brand-obsidian">
    <div class="max-w-6xl mx-auto">
      <div class="text-center mb-24">
        <div class="text-brand-amber font-black tracking-[0.5em] uppercase text-xs mb-4">The Visionaries</div>
        <h2 class="text-5xl md:text-7xl font-black text-white mb-6 tracking-tighter">THE PIONEERS</h2>
        <div class="w-24 h-1 bg-brand-amber mx-auto"></div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-16">
        <div v-for="speaker in speakers" :key="speaker.id" class="group relative flex flex-col md:flex-row items-center gap-10 p-10 rounded-[3rem] bg-white/5 border border-white/5 hover:border-brand-gold/20 transition-all hover:-translate-y-2 backdrop-blur-3xl overflow-hidden">
          <div class="absolute inset-0 bg-gradient-to-br from-brand-gold/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
          
          <div class="relative w-56 h-56 shrink-0 overflow-hidden rounded-[2rem] border-2 border-white/10 group-hover:border-brand-gold/40 transition-colors bg-white/5">
            <img v-if="speaker.image" :src="speaker.image" :alt="speaker.name" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110 grayscale group-hover:grayscale-0">
            <div v-else class="w-full h-full flex items-center justify-center text-white/10">
               <span class="font-black text-4xl">{{ speaker.name.charAt(0) }}</span>
            </div>
          </div>
          <div class="relative z-10 text-center md:text-left">
            <h3 class="text-3xl font-black text-white mb-2 tracking-tight">{{ speaker.name }}</h3>
            <p class="text-brand-gold font-black text-xs uppercase tracking-[0.2em] mb-6">{{ speaker.role }}</p>
            <p class="text-brand-mist/40 leading-relaxed font-light text-lg">{{ speaker.bio }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>