import { CONFIG } from "../core/config";

export default function Dashboard() {
    const username = "Admin";

    return (
        <div>
            <div>

            </div>
            <h1>Welcome back, <span>{username}</span></h1>
            <p>
                Welcome to the {CONFIG.COMPANY_NAME} ERP Portal.
                Select a module from sidebar to get started with an operation.
            </p>
        </div>
    );
}