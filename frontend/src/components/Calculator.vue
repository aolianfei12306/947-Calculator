<template>
  <div class="calculator">
    <div class="display">{{ display }}</div>
    <div class="buttons">
      <button
        v-for="btn in buttons"
        :key="btn.label"
        :class="['btn', btn.class]"
        @click="handleClick(btn)"
      >
        {{ btn.label }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const display = ref('0')
const currentValue = ref('')
const previousValue = ref('')
const operator = ref(null)
const shouldResetDisplay = ref(false)

const buttons = [
  { label: 'C', class: 'btn-operator', action: 'clear' },
  { label: '±', class: 'btn-operator', action: 'negate' },
  { label: '%', class: 'btn-operator', action: 'percent' },
  { label: '÷', class: 'btn-operator', action: 'operator', value: '/' },
  { label: '7', class: 'btn-number', action: 'number', value: '7' },
  { label: '8', class: 'btn-number', action: 'number', value: '8' },
  { label: '9', class: 'btn-number', action: 'number', value: '9' },
  { label: '×', class: 'btn-operator', action: 'operator', value: '*' },
  { label: '4', class: 'btn-number', action: 'number', value: '4' },
  { label: '5', class: 'btn-number', action: 'number', value: '5' },
  { label: '6', class: 'btn-number', action: 'number', value: '6' },
  { label: '−', class: 'btn-operator', action: 'operator', value: '-' },
  { label: '1', class: 'btn-number', action: 'number', value: '1' },
  { label: '2', class: 'btn-number', action: 'number', value: '2' },
  { label: '3', class: 'btn-number', action: 'number', value: '3' },
  { label: '+', class: 'btn-operator', action: 'operator', value: '+' },
  { label: '0', class: 'btn-number btn-zero', action: 'number', value: '0' },
  { label: '.', class: 'btn-number', action: 'decimal' },
  { label: '=', class: 'btn-equal', action: 'equals' }
]

function handleClick(btn) {
  switch (btn.action) {
    case 'number':
      inputNumber(btn.value)
      break
    case 'operator':
      inputOperator(btn.value)
      break
    case 'equals':
      calculate()
      break
    case 'clear':
      clear()
      break
    case 'negate':
      negate()
      break
    case 'percent':
      percent()
      break
    case 'decimal':
      inputDecimal()
      break
  }
}

function inputNumber(num) {
  if (shouldResetDisplay.value) {
    display.value = num
    shouldResetDisplay.value = false
  } else {
    display.value = display.value === '0' ? num : display.value + num
  }
  currentValue.value = display.value
}

function inputOperator(op) {
  if (operator.value && !shouldResetDisplay.value) {
    calculate()
  }
  previousValue.value = display.value
  operator.value = op
  shouldResetDisplay.value = true
}

function calculate() {
  if (!operator.value || previousValue.value === '') return

  const prev = parseFloat(previousValue.value)
  const current = parseFloat(display.value)
  let result

  switch (operator.value) {
    case '+':
      result = prev + current
      break
    case '-':
      result = prev - current
      break
    case '*':
      result = prev * current
      break
    case '/':
      result = current !== 0 ? prev / current : 'Error'
      break
  }

  display.value = result === 'Error' ? 'Error' : String(parseFloat(result.toFixed(10)))
  operator.value = null
  previousValue.value = ''
  shouldResetDisplay.value = true
}

function clear() {
  display.value = '0'
  currentValue.value = ''
  previousValue.value = ''
  operator.value = null
  shouldResetDisplay.value = false
}

function negate() {
  if (display.value !== '0' && display.value !== 'Error') {
    display.value = String(-parseFloat(display.value))
  }
}

function percent() {
  if (display.value !== 'Error') {
    display.value = String(parseFloat(display.value) / 100)
  }
}

function inputDecimal() {
  if (shouldResetDisplay.value) {
    display.value = '0.'
    shouldResetDisplay.value = false
  } else if (!display.value.includes('.')) {
    display.value += '.'
  }
}
</script>

<style scoped>
.calculator {
  width: 320px;
  margin: 80px auto;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
  background: #1c1c1c;
}

.display {
  padding: 24px 20px;
  text-align: right;
  font-size: 48px;
  font-weight: 300;
  color: #fff;
  background: #1c1c1c;
  min-height: 80px;
  display: flex;
  align-items: flex-end;
  justify-content: flex-end;
  word-break: break-all;
  line-height: 1.2;
}

.buttons {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1px;
  padding: 1px;
  background: #333;
}

.btn {
  border: none;
  padding: 20px;
  font-size: 24px;
  cursor: pointer;
  transition: background 0.15s;
  outline: none;
}

.btn:active {
  opacity: 0.7;
}

.btn-number {
  background: #505050;
  color: #fff;
}

.btn-number:hover {
  background: #666;
}

.btn-operator {
  background: #ff9f0a;
  color: #fff;
}

.btn-operator:hover {
  background: #ffb340;
}

.btn-equal {
  background: #ff9f0a;
  color: #fff;
}

.btn-equal:hover {
  background: #ffb340;
}

.btn-zero {
  grid-column: span 2;
  text-align: left;
  padding-left: 32px;
}
</style>
