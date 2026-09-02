import { DashboardCard } from "@/components/dashboard-card";
import { MessageSquare, Users, Bot, CheckCircle } from "lucide-react";

export default function DashboardPage() {
  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-6">Dashboard</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <DashboardCard title="Total Conversations" value="1,284" icon={MessageSquare} />
        <DashboardCard title="Open Conversations" value="32" icon={MessageSquare} />
        <DashboardCard title="AI Replies" value="847" icon={Bot} />
        <DashboardCard title="Customers" value="923" icon={Users} />
      </div>
    </div>
  );
}
