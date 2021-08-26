#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: v3.8.2.0-57-gd71cd177

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
import osmosdr
import time

from gnuradio import qtgui

class fmcw_simulado_01(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "fmcw_simulado_01")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.sample_delay_rx = sample_delay_rx = 100
        self.samp_rate = samp_rate = 2e6
        self.gain_tx = gain_tx = 10
        self.gain_rx = gain_rx = 10
        self.amp_tx = amp_tx = 0.1
        self.amp_rx = amp_rx = 10
        self.PI = PI = 3.14159
        self.FC_TX = FC_TX = 2.4e9
        self.FC_RX = FC_RX = 2.4e9

        ##################################################
        # Blocks
        ##################################################
        self._gain_tx_range = Range(0, 20, 1, 10, 200)
        self._gain_tx_win = RangeWidget(self._gain_tx_range, self.set_gain_tx, 'GAIN TX', "counter_slider", float)
        self.top_grid_layout.addWidget(self._gain_tx_win)
        self._gain_rx_range = Range(0, 20, 1, 10, 200)
        self._gain_rx_win = RangeWidget(self._gain_rx_range, self.set_gain_rx, 'GAIN RX', "counter_slider", float)
        self.top_grid_layout.addWidget(self._gain_rx_win)
        self._amp_tx_range = Range(0.05, 1, 0.05, 0.1, 200)
        self._amp_tx_win = RangeWidget(self._amp_tx_range, self.set_amp_tx, 'AMP TX', "counter_slider", float)
        self.top_grid_layout.addWidget(self._amp_tx_win)
        self._amp_rx_range = Range(10, 500, 10, 10, 200)
        self._amp_rx_win = RangeWidget(self._amp_rx_range, self.set_amp_rx, 'AMP RX', "counter_slider", float)
        self.top_grid_layout.addWidget(self._amp_rx_win)
        self._sample_delay_rx_range = Range(0, 50e3, 100, 100, 200)
        self._sample_delay_rx_win = RangeWidget(self._sample_delay_rx_range, self.set_sample_delay_rx, 'Delay TX', "counter_slider", float)
        self.top_grid_layout.addWidget(self._sample_delay_rx_win)
        self.qtgui_sink_x_0_1 = qtgui.sink_c(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate/2000, #bw
            "FFT Resampler", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True #plotconst
        )
        self.qtgui_sink_x_0_1.set_update_time(1.0/10)
        self._qtgui_sink_x_0_1_win = sip.wrapinstance(self.qtgui_sink_x_0_1.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_1.enable_rf_freq(False)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_1_win)
        self.osmosdr_source_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + ""
        )
        self.osmosdr_source_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(FC_RX, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(gain_rx, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + ""
        )
        self.osmosdr_sink_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(FC_TX, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(gain_tx, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
        self.hilbert_fc_0 = filter.hilbert_fc(64, firdes.WIN_HAMMING, 6.76)
        self.dc_blocker_xx_0 = filter.dc_blocker_cc(32, True)
        self.blocks_vco_f_1 = blocks.vco_f(samp_rate, 1e6, 1)
        self.blocks_throttle_1_0_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, 1e6,True)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_cc(amp_tx)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(amp_rx)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_delay_1 = blocks.delay(gr.sizeof_gr_complex*1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, 0.04, 2*PI, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_vco_f_1, 0))
        self.connect((self.blocks_delay_1, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.blocks_throttle_1_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_throttle_1_0_0_0, 0), (self.qtgui_sink_x_0_1, 0))
        self.connect((self.blocks_vco_f_1, 0), (self.hilbert_fc_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.hilbert_fc_0, 0), (self.blocks_delay_1, 0))
        self.connect((self.hilbert_fc_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.dc_blocker_xx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fmcw_simulado_01")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sample_delay_rx(self):
        return self.sample_delay_rx

    def set_sample_delay_rx(self, sample_delay_rx):
        self.sample_delay_rx = sample_delay_rx

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 0.6e6, 1e3, firdes.WIN_HAMMING, 6.76))
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.qtgui_sink_x_0_1.set_frequency_range(0, self.samp_rate/2000)

    def get_gain_tx(self):
        return self.gain_tx

    def set_gain_tx(self, gain_tx):
        self.gain_tx = gain_tx
        self.osmosdr_sink_0.set_gain(self.gain_tx, 0)

    def get_gain_rx(self):
        return self.gain_rx

    def set_gain_rx(self, gain_rx):
        self.gain_rx = gain_rx
        self.osmosdr_source_0.set_gain(self.gain_rx, 0)

    def get_amp_tx(self):
        return self.amp_tx

    def set_amp_tx(self, amp_tx):
        self.amp_tx = amp_tx
        self.blocks_multiply_const_vxx_0_0.set_k(self.amp_tx)

    def get_amp_rx(self):
        return self.amp_rx

    def set_amp_rx(self, amp_rx):
        self.amp_rx = amp_rx
        self.blocks_multiply_const_vxx_0.set_k(self.amp_rx)

    def get_PI(self):
        return self.PI

    def set_PI(self, PI):
        self.PI = PI
        self.analog_sig_source_x_0.set_amplitude(2*self.PI)

    def get_FC_TX(self):
        return self.FC_TX

    def set_FC_TX(self, FC_TX):
        self.FC_TX = FC_TX
        self.osmosdr_sink_0.set_center_freq(self.FC_TX, 0)

    def get_FC_RX(self):
        return self.FC_RX

    def set_FC_RX(self, FC_RX):
        self.FC_RX = FC_RX
        self.osmosdr_source_0.set_center_freq(self.FC_RX, 0)





def main(top_block_cls=fmcw_simulado_01, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
