define([
    "dojo/_base/declare",
    "dojo/promise/all",
    "pico/control/WrappedWidget",
    "pico/layout/GridContainer",
    "pico/widget",
    "pico/datastore",
    "pico/expr"
], function(declare, all, WrappedWidget, GridContainer, pwidget, datastore, 
        pexpr) {


/**
 * Displays information about a single process
 *
 * Config Attributes
 * =================
 * PID (integer): PID for the process to view
 **/
var ProcessDetail = declare([WrappedWidget], {

    constructor: function() {
        this.delegate = new GridContainer();
        this._filter = null;
    },

    init$: function() {
        var self = this;
        var cfg = this.getConfig();
        var pid = cfg.getAsInteger("PID");

        if(!pid || pid <= 0) {
            throw "A valid process ID is required";
        }

        this._filter = pexpr.parse('PID === ' + pid);

        return datastore.query$('select Name, PID from Sysmon.Process where ' + 
            this._filter.serialize())
        .then(function(result) {
            return self._show$(result.get(0));
        });
    },

    _show$: function(process) {
        var self = this;
        var grid = this.delegate;

        var rows = grid.addRows([
            { height: "150px" },
            { height: "auto" }
        ]);

        // 2 rows of the same height
        var chartRows = rows[1].addRows(2);

        return pwidget.findAll$([
            { name: "Sysmon.ProcessDetail" },
            { name: "Sysmon.SingleProcessCPUChart" },
            { name: "Sysmon.SingleProcessMemChart" }
        ]).then(function(widgets) {

            var pname = process.getAsString("Name");
            var pid = process.getAsInteger("PID");

            var detailWidget = widgets[0];
            detailWidget.updateConfig({
                Title: "Process: " + pname,
            });

            var cpuChart = widgets[1];
            var memChart = widgets[2];

            detailWidget.setFilter(self._filter);
            cpuChart.setFilter(self._filter);
            memChart.setFilter(self._filter);

            return grid.startup$(self.getNode())
            .then(function() {
                return all([
                    rows[0].loadWidget$(widgets[0]),
                    chartRows[0].loadWidget$(widgets[1]),
                    chartRows[1].loadWidget$(widgets[2])
                ]);
            });

        });
    }

});


/**
 * An action handler to pop up a dialog with process details
 */
ProcessDetail.handleShowAction = function(properties) {
    var type = properties.type;
    var filter = properties.selection;

    datastore.find$(type.getAsString("ForType"), filter)
    .then(function(result) {
        var process = result.get(0);
        
        if(process) {
            var pname = process.getAsString("Name");
            var pid = process.getAsInteger("PID");
            pwidget.displayInDialog$({
                Plugin: "sysmon/process/advanced/ProcessDetail",
                PID: pid,
                Container: {
                    Title: "Details for " + pname + " (PID " + pid + ")",
                    Padded: true,
                    SizeToFit: false,
                    Width: 800,
                    Height: 600,
                    CloseButtonText: "Close"
                }
            });
        } else {
            console.warn("Unable to find submission matching " + filter);
        }
    });
};


return ProcessDetail;


});