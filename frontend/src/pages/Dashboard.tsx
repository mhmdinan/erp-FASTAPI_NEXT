import { CONFIG } from "../core/config";
import TopBar from "../components/layout/TopBar";

export default function Dashboard() {
    const username = "Admin";

    return (
        <div>
            <div>
                <TopBar></TopBar>
            </div>
            <h1>Welcome back, <span>{username}</span></h1>
            <p>
                Welcome to the {CONFIG.COMPANY_NAME} ERP Portal.
                Select a module from sidebar to get started with an operation.
            </p>
        </div>
    );
}