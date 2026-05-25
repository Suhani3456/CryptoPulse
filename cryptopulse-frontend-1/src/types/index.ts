export type CryptoAsset = {
    id: string;
    name: string;
    symbol: string;
    price: number;
    marketCap: number;
    volume: number;
    changePercentage: number;
};

export type PortfolioItem = {
    asset: CryptoAsset;
    quantity: number;
};

export type UserPortfolio = {
    id: string;
    items: PortfolioItem[];
};

export type AnalyticsData = {
    totalInvested: number;
    totalValue: number;
    profitLoss: number;
    performance: {
        date: string;
        value: number;
    }[];
};