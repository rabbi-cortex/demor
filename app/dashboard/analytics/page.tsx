"use client";

import { DashboardCard } from "@/components/dashboard-card";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

const data = [
  { name: "Mon", conversations: 40 },
  { name: "Tue", conversations: 30 },
  { name: "Wed", conversations: 50 },
  { name: "Thu", conversations: 25 },
  { name: "Fri", conversations: 60 },
];

export default function AnalyticsPage() {
  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-6">Analytics</h1>
      <div className="h-64 bg-card p-4 rounded-lg border border-border">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data}>
            <XAxis dataKey="name" stroke="#666" />
            <YAxis stroke="#666" />
            <Tooltip contentStyle={{ backgroundColor: "#000", border: "none" }} />
            <Bar dataKey="conversations" fill="#00FF88" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
