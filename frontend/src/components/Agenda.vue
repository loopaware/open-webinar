<script setup lang="ts">
import { Clock, Zap } from 'lucide-vue-next'

defineProps<{
  items: any[]
}>()
</script>

<template>
  <section id="agenda" class="py-32 px-6 bg-brand-obsidian relative overflow-hidden">
    <!-- Premium Atmosphere -->
    <div class="absolute top-0 right-0 w-[600px] h-[600px] bg-brand-gold/5 rounded-full blur-[120px] -mr-64 -mt-64"></div>
    
    <div class="max-w-5xl mx-auto relative z-10">
      <div class="text-center mb-24">
        <div class="text-brand-gold font-black tracking-[0.5em] uppercase text-xs mb-4">The Schedule</div>
        <h2 class="text-5xl md:text-7xl font-black text-white mb-6 tracking-tighter">PHASE LOG</h2>
        <div class="w-24 h-1 bg-brand-gold mx-auto"></div>
      </div>

      <div class="space-y-4">
        <div v-for="(item, index) in items" :key="item.id" 
          :class="[
            'group flex flex-col md:flex-row items-start md:items-center gap-6 p-8 md:p-10 rounded-[2rem] transition-all border-2 backdrop-blur-2xl',
            index % 2 === 1 ? 'bg-white/5 border-brand-gold/30 shadow-[0_0_50px_rgba(251,191,36,0.05)]' : 'bg-transparent border-white/5 hover:border-white/10'
          ]">
          <div :class="['font-mono font-black text-3xl md:text-4xl tracking-tighter', index % 2 === 1 ? 'text-brand-gold' : 'text-white/20']">
            {{ item.time }}
          </div>
          <div class="flex-1">
            <div :class="['text-[10px] uppercase font-black tracking-[0.3em] mb-2', index % 2 === 1 ? 'text-brand-amber' : 'text-brand-gold/40']">
              {{ item.speaker_name || 'Protocol' }}
            </div>
            <div class="text-xl md:text-2xl font-black text-white tracking-tight group-hover:text-brand-gold transition-colors">
              {{ item.title }}
            </div>
            <p v-if="item.description" class="mt-4 text-brand-mist/40 font-light text-sm leading-relaxed max-w-2xl">
              {{ item.description }}
            </p>
          </div>
          <Zap v-if="index % 2 === 1" class="w-8 h-8 text-brand-gold animate-pulse" />
          <Clock v-else class="w-6 h-6 text-white/10" />
        </div>
      </div>
    </div>
  </section>
</template>