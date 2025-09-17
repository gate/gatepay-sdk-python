from typing import Optional, Dict
from dataclasses import dataclass, field

from src.gatepay.base_response import BaseResponse


@dataclass
class QueryBalanceResp(BaseResponse['QueryBalanceResp']):
    def __init__(self):
        super().__init__()
        # 确保所有属性都被初始化

    # 使用字典存储所有币种余额，而不是为每个币种创建单独的属性
    balances: Dict[str, Optional[str]] = field(default_factory=dict)

    def __post_init__(self):
        """
        初始化后处理
        """
        # 初始化所有币种余额为None
        coin_types = [
            "ALGO", "APT", "ARB", "ATOM", "AVAX", "BCH", "BNB", "BTC", "CRO", "DAI",
            "DOGE", "EEG", "ETC", "ETH", "FDUSD", "FET", "HBAR", "ICP", "KAS", "LEO",
            "LINK", "LION", "MKR", "MNT", "NEAR", "PEPE", "POL", "PPIE", "RENDER",
            "SEPOLIA", "SHIB", "SOL", "STX", "TAO", "TESTNET3", "TON", "TRX", "UNI",
            "USDC", "USDT", "VET", "XLM", "XMR"
        ]
        for coin in coin_types:
            if coin not in self.balances:
                self.balances[coin] = None

    def get_balance(self, coin_type: str) -> Optional[str]:
        """
        获取指定币种的余额

        :param coin_type: 币种类型
        :return: 余额
        """
        return self.balances.get(coin_type)

    def set_balance(self, coin_type: str, balance: str) -> None:
        """
        设置指定币种的余额

        :param coin_type: 币种类型
        :param balance: 余额
        """
        self.balances[coin_type] = balance

    # 为常用币种提供便捷方法
    def get_algo(self) -> Optional[str]:
        """获取ALGO余额"""
        return self.balances.get("ALGO")

    def set_algo(self, algo: str) -> None:
        """设置ALGO余额"""
        self.balances["ALGO"] = algo

    def get_apt(self) -> Optional[str]:
        """获取APT余额"""
        return self.balances.get("APT")

    def set_apt(self, apt: str) -> None:
        """设置APT余额"""
        self.balances["APT"] = apt

    def get_arb(self) -> Optional[str]:
        """获取ARB余额"""
        return self.balances.get("ARB")

    def set_arb(self, arb: str) -> None:
        """设置ARB余额"""
        self.balances["ARB"] = arb

    def get_atom(self) -> Optional[str]:
        """获取ATOM余额"""
        return self.balances.get("ATOM")

    def set_atom(self, atom: str) -> None:
        """设置ATOM余额"""
        self.balances["ATOM"] = atom

    def get_avax(self) -> Optional[str]:
        """获取AVAX余额"""
        return self.balances.get("AVAX")

    def set_avax(self, avax: str) -> None:
        """设置AVAX余额"""
        self.balances["AVAX"] = avax

    def get_bch(self) -> Optional[str]:
        """获取BCH余额"""
        return self.balances.get("BCH")

    def set_bch(self, bch: str) -> None:
        """设置BCH余额"""
        self.balances["BCH"] = bch

    def get_bnb(self) -> Optional[str]:
        """获取BNB余额"""
        return self.balances.get("BNB")

    def set_bnb(self, bnb: str) -> None:
        """设置BNB余额"""
        self.balances["BNB"] = bnb

    def get_btc(self) -> Optional[str]:
        """获取BTC余额"""
        return self.balances.get("BTC")

    def set_btc(self, btc: str) -> None:
        """设置BTC余额"""
        self.balances["BTC"] = btc

    def get_cro(self) -> Optional[str]:
        """获取CRO余额"""
        return self.balances.get("CRO")

    def set_cro(self, cro: str) -> None:
        """设置CRO余额"""
        self.balances["CRO"] = cro

    def get_dai(self) -> Optional[str]:
        """获取DAI余额"""
        return self.balances.get("DAI")

    def set_dai(self, dai: str) -> None:
        """设置DAI余额"""
        self.balances["DAI"] = dai

    def get_doge(self) -> Optional[str]:
        """获取DOGE余额"""
        return self.balances.get("DOGE")

    def set_doge(self, doge: str) -> None:
        """设置DOGE余额"""
        self.balances["DOGE"] = doge

    def get_eeg(self) -> Optional[str]:
        """获取EEG余额"""
        return self.balances.get("EEG")

    def set_eeg(self, eeg: str) -> None:
        """设置EEG余额"""
        self.balances["EEG"] = eeg

    def get_etc(self) -> Optional[str]:
        """获取ETC余额"""
        return self.balances.get("ETC")

    def set_etc(self, etc: str) -> None:
        """设置ETC余额"""
        self.balances["ETC"] = etc

    def get_eth(self) -> Optional[str]:
        """获取ETH余额"""
        return self.balances.get("ETH")

    def set_eth(self, eth: str) -> None:
        """设置ETH余额"""
        self.balances["ETH"] = eth

    def get_fdusd(self) -> Optional[str]:
        """获取FDUSD余额"""
        return self.balances.get("FDUSD")

    def set_fdusd(self, fdusd: str) -> None:
        """设置FDUSD余额"""
        self.balances["FDUSD"] = fdusd

    def get_fet(self) -> Optional[str]:
        """获取FET余额"""
        return self.balances.get("FET")

    def set_fet(self, fet: str) -> None:
        """设置FET余额"""
        self.balances["FET"] = fet

    def get_hbar(self) -> Optional[str]:
        """获取HBAR余额"""
        return self.balances.get("HBAR")

    def set_hbar(self, hbar: str) -> None:
        """设置HBAR余额"""
        self.balances["HBAR"] = hbar

    def get_icp(self) -> Optional[str]:
        """获取ICP余额"""
        return self.balances.get("ICP")

    def set_icp(self, icp: str) -> None:
        """设置ICP余额"""
        self.balances["ICP"] = icp

    def get_kas(self) -> Optional[str]:
        """获取KAS余额"""
        return self.balances.get("KAS")

    def set_kas(self, kas: str) -> None:
        """设置KAS余额"""
        self.balances["KAS"] = kas

    def get_leo(self) -> Optional[str]:
        """获取LEO余额"""
        return self.balances.get("LEO")

    def set_leo(self, leo: str) -> None:
        """设置LEO余额"""
        self.balances["LEO"] = leo

    def get_link(self) -> Optional[str]:
        """获取LINK余额"""
        return self.balances.get("LINK")

    def set_link(self, link: str) -> None:
        """设置LINK余额"""
        self.balances["LINK"] = link

    def get_lion(self) -> Optional[str]:
        """获取LION余额"""
        return self.balances.get("LION")

    def set_lion(self, lion: str) -> None:
        """设置LION余额"""
        self.balances["LION"] = lion

    def get_mkr(self) -> Optional[str]:
        """获取MKR余额"""
        return self.balances.get("MKR")

    def set_mkr(self, mkr: str) -> None:
        """设置MKR余额"""
        self.balances["MKR"] = mkr

    def get_mnt(self) -> Optional[str]:
        """获取MNT余额"""
        return self.balances.get("MNT")

    def set_mnt(self, mnt: str) -> None:
        """设置MNT余额"""
        self.balances["MNT"] = mnt

    def get_near(self) -> Optional[str]:
        """获取NEAR余额"""
        return self.balances.get("NEAR")

    def set_near(self, near: str) -> None:
        """设置NEAR余额"""
        self.balances["NEAR"] = near

    def get_pepe(self) -> Optional[str]:
        """获取PEPE余额"""
        return self.balances.get("PEPE")

    def set_pepe(self, pepe: str) -> None:
        """设置PEPE余额"""
        self.balances["PEPE"] = pepe

    def get_pol(self) -> Optional[str]:
        """获取POL余额"""
        return self.balances.get("POL")

    def set_pol(self, pol: str) -> None:
        """设置POL余额"""
        self.balances["POL"] = pol

    def get_ppie(self) -> Optional[str]:
        """获取PPIE余额"""
        return self.balances.get("PPIE")

    def set_ppie(self, ppie: str) -> None:
        """设置PPIE余额"""
        self.balances["PPIE"] = ppie

    def get_render(self) -> Optional[str]:
        """获取RENDER余额"""
        return self.balances.get("RENDER")

    def set_render(self, render: str) -> None:
        """设置RENDER余额"""
        self.balances["RENDER"] = render

    def get_sepolia(self) -> Optional[str]:
        """获取SEPOLIA余额"""
        return self.balances.get("SEPOLIA")

    def set_sepolia(self, sepolia: str) -> None:
        """设置SEPOLIA余额"""
        self.balances["SEPOLIA"] = sepolia

    def get_shib(self) -> Optional[str]:
        """获取SHIB余额"""
        return self.balances.get("SHIB")

    def set_shib(self, shib: str) -> None:
        """设置SHIB余额"""
        self.balances["SHIB"] = shib

    def get_sol(self) -> Optional[str]:
        """获取SOL余额"""
        return self.balances.get("SOL")

    def set_sol(self, sol: str) -> None:
        """设置SOL余额"""
        self.balances["SOL"] = sol

    def get_stx(self) -> Optional[str]:
        """获取STX余额"""
        return self.balances.get("STX")

    def set_stx(self, stx: str) -> None:
        """设置STX余额"""
        self.balances["STX"] = stx

    def get_tao(self) -> Optional[str]:
        """获取TAO余额"""
        return self.balances.get("TAO")

    def set_tao(self, tao: str) -> None:
        """设置TAO余额"""
        self.balances["TAO"] = tao

    def get_testnet3(self) -> Optional[str]:
        """获取TESTNET3余额"""
        return self.balances.get("TESTNET3")

    def set_testnet3(self, testnet3: str) -> None:
        """设置TESTNET3余额"""
        self.balances["TESTNET3"] = testnet3

    def get_ton(self) -> Optional[str]:
        """获取TON余额"""
        return self.balances.get("TON")

    def set_ton(self, ton: str) -> None:
        """设置TON余额"""
        self.balances["TON"] = ton

    def get_trx(self) -> Optional[str]:
        """获取TRX余额"""
        return self.balances.get("TRX")

    def set_trx(self, trx: str) -> None:
        """设置TRX余额"""
        self.balances["TRX"] = trx

    def get_uni(self) -> Optional[str]:
        """获取UNI余额"""
        return self.balances.get("UNI")

    def set_uni(self, uni: str) -> None:
        """设置UNI余额"""
        self.balances["UNI"] = uni

    def get_usdc(self) -> Optional[str]:
        """获取USDC余额"""
        return self.balances.get("USDC")

    def set_usdc(self, usdc: str) -> None:
        """设置USDC余额"""
        self.balances["USDC"] = usdc

    def get_usdt(self) -> Optional[str]:
        """获取USDT余额"""
        return self.balances.get("USDT")

    def set_usdt(self, usdt: str) -> None:
        """设置USDT余额"""
        self.balances["USDT"] = usdt

    def get_vet(self) -> Optional[str]:
        """获取VET余额"""
        return self.balances.get("VET")

    def set_vet(self, vet: str) -> None:
        """设置VET余额"""
        self.balances["VET"] = vet

    def get_xlm(self) -> Optional[str]:
        """获取XLM余额"""
        return self.balances.get("XLM")

    def set_xlm(self, xlm: str) -> None:
        """设置XLM余额"""
        self.balances["XLM"] = xlm

    def get_xmr(self) -> Optional[str]:
        """获取XMR余额"""
        return self.balances.get("XMR")

    def set_xmr(self, xmr: str) -> None:
        """设置XMR余额"""
        self.balances["XMR"] = xmr
